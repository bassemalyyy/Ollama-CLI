# Ollama CLI with Custom Tools

A command-line interface for interacting with local Ollama models with integrated custom tools for enhanced functionality.

## Features

- 🤖 Chat with any Ollama model locally
- 🔍 Web search capabilities via Serper.dev
- 🌤️ Weather information via OpenWeatherMap
- 📍 Location detection based on IP
- 🕒 Time and date information
- 📁 File tools integration via Composio (optional)
- 🔧 Flexible tool configuration

## Installation

1. **Install Ollama**: https://ollama.ai/
2. **Clone this repository**
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Install the package**: `pip install -e .`

## API Keys Setup

To use all features, you'll need to set up these environment variables:

```bash
# For web search functionality
export SERPER_API_KEY="your_serper_api_key"  # Get from https://serper.dev

# For weather information
export OPENWEATHERMAP_API_KEY="your_openweather_api_key"  # Get from https://openweathermap.org/api
```

## Usage

### Basic Usage
```bash
ollama_cli
```

### Advanced Usage
```bash
# Use a specific model
ollama_cli --model llama3.1:70b

# Use custom Ollama URL
ollama_cli --base-url http://192.168.1.100:11434

# Disable all tools
ollama_cli --no-tools

# Disable only Composio file tools
ollama_cli --no-composio

# Disable only custom tools
ollama_cli --no-custom-tools

# List available models
ollama_cli --list-models
```

## Available Tools

### 1. Web Search
- **Command**: Ask questions that require current information
- **Example**: "Search for latest AI news" or "What's happening in the world?"
- **Requires**: `SERPER_API_KEY` environment variable

### 2. Weather Information
- **Command**: Ask about weather conditions
- **Example**: "What's the weather in London?" or "How's the weather?"
- **Requires**: `OPENWEATHERMAP_API_KEY` environment variable

### 3. Location Detection
- **Command**: Ask about your location
- **Example**: "Where am I?" or "What's my location?"
- **Requires**: `geocoder` package (auto-installed)

### 4. Time Information
- **Command**: Ask about current time
- **Example**: "What time is it?" or "What's the date?"
- **Requires**: `pytz` package (auto-installed)

### 5. File Operations (Optional)
- **Command**: File-related operations
- **Example**: "Create a file" or "Read this document"
- **Requires**: Composio setup

## Prerequisites

1. **Ollama**: Make sure Ollama is installed and running
   ```bash
   ollama serve
   ```

2. **Model**: Pull your desired model
   ```bash
   ollama pull llama3.1:8b
   ```

3. **API Keys**: Set up environment variables for external services

## Example Interactions

```bash
You: What's the weather in New York?
Assistant: 🌡️ Temperature: 22°C (feels like 25°C)
🌤️ Condition: Partly cloudy
💧 Humidity: 65%

You: Search for latest Python releases
Assistant: Search results for 'latest Python releases' (as of 2024-01-15 10:30:00):

1. Python 3.12.1 Released
URL: https://www.python.org/downloads/release/python-3121/
Description: The latest bugfix release for Python 3.12...

You: What time is it?
Assistant: Current time in Egypt (Cairo): 2024-01-15 10:30:45

You: Where am I?
Assistant: Your current location: New York, NY, United States
```

## Common Models

- `llama3.1:8b` - Fast and efficient
- `llama3.1:70b` - More capable but slower
- `codellama:7b` - Optimized for coding
- `mistral:7b` - Alternative model

## Troubleshooting

### Connection Issues
- **"Cannot connect to Ollama"**: Make sure Ollama is running with `ollama serve`
- **"Model not found"**: Pull the model with `ollama pull <model-name>`

### API Key Issues
- **"Search API key not configured"**: Set `SERPER_API_KEY` environment variable
- **"Weather API key not configured"**: Set `OPENWEATHERMAP_API_KEY` environment variable

### Tool Issues
- **"geocoder package not installed"**: Install with `pip install geocoder`
- **"pytz package not installed"**: Install with `pip install pytz`
- **Composio tools not working**: Install with `pip install composio_core composio_langchain`

### Getting API Keys

1. **Serper.dev** (Web Search):
   - Visit https://serper.dev
   - Sign up for free account
   - Get your API key from dashboard

2. **OpenWeatherMap** (Weather):
   - Visit https://openweathermap.org/api
   - Sign up for free account
   - Get your API key from account settings

## Development

To contribute or modify the tools:

1. **Add new tools**: Create new files in `ollama_cli/tools/`
2. **Modify existing tools**: Edit files in `ollama_cli/tools/`
3. **Update agent**: Modify `ollama_cli/agent.py` to include new tools
4. **Test changes**: Run `ollama_cli` to test your modifications

## License

MIT License - feel free to use and modify as needed.