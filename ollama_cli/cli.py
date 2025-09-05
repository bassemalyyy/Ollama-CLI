import click
from .agent import OllamaAgent

@click.command()
@click.option('--model', default="llama3.2:latest", help='Ollama model name (default: llama3.2:latest)')
@click.option('--base-url', default="http://localhost:11434", help='Ollama base URL (default: http://localhost:11434)')
@click.option('--list-models', is_flag=True, help='List available Ollama models')

def main(model, base_url, list_models):
    if list_models:
        try:
            import requests
            response = requests.get(f"{base_url}/api/tags")
            if response.status_code == 200:
                models = response.json().get('models', [])
                print("Available Ollama models:")
                for model_info in models:
                    print(f"  - {model_info['name']}")
                return
            else:
                print("❌ Could not retrieve models from Ollama")
                return
        except Exception as e:
            print(f"❌ Error connecting to Ollama: {e}")
            return
    
    # Initialize agent
    agent = OllamaAgent(llm=model, base_url=base_url)
    
    # ASCII Art for Ollama CLI
    print("""
 ██████╗ ██╗     ██╗      █████╗ ███╗   ███╗ █████╗      ██████╗██╗     ██╗
██╔═══██╗██║     ██║     ██╔══██╗████╗ ████║██╔══██╗    ██╔════╝██║     ██║
██║   ██║██║     ██║     ███████║██╔████╔██║███████║    ██║     ██║     ██║
██║   ██║██║     ██║     ██╔══██║██║╚██╔╝██║██╔══██║    ██║     ██║     ██║
╚██████╔╝███████╗███████╗██║  ██║██║ ╚═╝ ██║██║  ██║    ╚██████╗███████╗██║
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝
    """)
    print(f"Chat with {model} running locally via Ollama.")
    print("Type 'exit' to quit.")
    
    # Check Ollama connection
    is_connected, status_msg = agent.check_ollama_connection()
    print(status_msg)
    
    if not is_connected:
        print("\n💡 To start Ollama, run: ollama serve")
        print(f"💡 To pull the model, run: ollama pull {model}")
        return
    
    # Display tool status
    print("\n🔧 Tools are enabled via .bind_tools()")
    
    print("\n" + "="*50)
    
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            if user_input.strip():
                agent.chat(user_input)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break