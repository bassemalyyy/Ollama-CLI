from langchain_core.messages import HumanMessage, ToolMessage
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import requests
import json
from .tools import location, search, Time, get_weather

class OllamaAgent:
    """A conversational agent that interacts with an Ollama model."""

    def __init__(self, llm: str = "llama3.2:latest", base_url: str = "http://localhost:11434"):
        # The prompt template that provides instructions to the LLM
        prompt_template = ChatPromptTemplate.from_messages([
            ("system",
             "You are Titan, a helpful personal assistant. You have access to a variety of tools to answer user questions.\n"
             "For questions about the current weather, use the 'get_weather' tool.\n"
             "For questions about your current location, use the 'location' tool.\n"
             "For general information and web searches, use the 'search' tool.\n"
             "For the current time, use the 'Time' tool.\n"
             "If you cannot find an answer using the provided tools, respond with a polite message stating you cannot assist with that request."),
            ("placeholder", "{messages}"),
        ])
        
        self.model = ChatOllama(model=llm, base_url=base_url)
        self.base_url = base_url
        
        # Bind the tools to the model and create the runnable chain
        self.chain = prompt_template | self.model.bind_tools(
            tools=[location, search, Time, get_weather]
        )
        
        self.tools = {
            "location": location,
            "search": search,
            "Time": Time,
            "get_weather": get_weather
        }

    def check_ollama_connection(self) -> tuple[bool, str]:
        """Checks if the Ollama service and the specified model are available."""
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            if response.status_code == 200:
                models = [m['name'] for m in response.json().get('models', [])]
                if self.model.model in models:
                    return True, "✅ Successfully connected to Ollama and model is available."
                else:
                    return False, f"❌ Model '{self.model.model}' not found. Please pull it using 'ollama pull {self.model.model}'."
            else:
                return False, f"❌ Failed to connect to Ollama at {self.base_url}. Status code: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return False, f"❌ Connection Error: {e}. Is Ollama running?"

    def chat(self, user_input: str):
        """Processes user input and generates a response using the tool-bound model."""
        try:
            # First invoke: get the LLM's initial response
            response = self.chain.invoke({"messages": [HumanMessage(content=user_input)]})
            
            tool_calls = response.tool_calls
            
            # Fallback: check if the response content is a tool call JSON string
            if not tool_calls and response.content.strip().startswith('{') and response.content.strip().endswith('}'):
                try:
                    # Attempt to parse the raw JSON string
                    parsed_response = json.loads(response.content)
                    if 'name' in parsed_response and 'parameters' in parsed_response:
                        tool_calls = [{
                            'name': parsed_response['name'],
                            'args': parsed_response['parameters'],
                            'id': 'manual_call' # Assign a dummy ID
                        }]
                except json.JSONDecodeError:
                    pass # Not a valid JSON, continue to next part
            
            # Check if we have tool calls (either from object or manual parsing)
            if tool_calls:
                tool_output_messages = []
                for tool_call in tool_calls:
                    tool_name = tool_call['name']
                    tool_args = tool_call['args']
                    
                    if tool_name in self.tools:
                        print(f"\nTitan is thinking... 🧠")
                        
                        # Execute the tool and get the result
                        tool_output = self.tools[tool_name](**tool_args)
                        
                        # Create a ToolMessage from the output
                        tool_output_messages.append(
                            ToolMessage(content=str(tool_output), tool_call_id=tool_call['id'])
                        )
                
                # Create a list of messages to pass back to the LLM
                messages = [
                    HumanMessage(content=user_input),
                    response, # The tool call from the LLM
                    *tool_output_messages, # The outputs from the tools
                ]

                # Second invoke: pass the tool output back to the LLM to get the final answer
                final_response = self.chain.invoke({"messages": messages})
                
                print(f"Titan: {final_response.content}")
                return
            
            # If no tool calls, display the response content
            print(f"Titan: {response.content}")
            
        except Exception as e:
            print(f"An error occurred: {e}")