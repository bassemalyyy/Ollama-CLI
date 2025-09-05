Ollama CLI with Custom Tools
============================

A command-line interface for interacting with local Ollama models with integrated custom tools for enhanced functionality.

Features
--------

-   🤖  Chat with any Ollama model locally

-   🔍 Web search capabilities via Serper.dev

-   🌤️ Weather information via OpenWeatherMap

-   🗺️ Location detection based on IP

-   🕒 Time and date information for any city in Egypt

-   🔧 Flexible tool configuration

* * * * *

Installation
------------

1.  **Install Ollama**: Follow the instructions at <https://ollama.ai/>

2.  **Clone this repository**

3.  **Install dependencies**: `pip install -r requirements.txt`

4.  **Install the package**: `pip install -e .`

* * * * *

API Keys Setup
--------------

To use all features, you'll need to set up these environment variables in a `.env` file in the root directory:

Bash

```bash
# For web search functionality
SERPER_API_KEY="your_serper_api_key"

# For weather information
OPENWEATHERMAP_API_KEY="your_openweather_api_key"
```

* * * * *

Usage
-----

### Basic Usage

Bash

```bash
ollama_cli
```

### Advanced Usage

Bash

```bash
# Use a specific model
ollama_cli --model llama3.1:70b

# Use custom Ollama URL
ollama_cli --base-url http://192.168.1.100:11434
```

* * * * *

Available Tools
---------------

### 1\. Web Search

-   **Command**: Ask questions that require current information.

-   **Example**: "Search for latest AI news" or "What's happening in the world?"

-   **Requires**: `SERPER_API_KEY` environment variable.

### 2\. Weather Information

-   **Command**: Ask about weather conditions for a specific location.

-   **Example**: "What's the weather in Alexandria?"

-   **Requires**: `OPENWEATHERMAP_API_KEY` environment variable.

### 3\. Location Detection

-   **Command**: Ask about your current location.

-   **Example**: "Where am I?" or "What's my location?"

-   **Requires**: No extra setup.

### 4\. Time Information

-   **Command**: Ask about the current time in any Egyptian city.

-   **Example**: "What is the time in Cairo?" or "What's the time in Alexandria?"

-   **Requires**: No extra setup.

* * * * *

Prerequisites
-------------

1.  **Ollama**: Make sure Ollama is installed and running.

    Bash

    ```bash
    ollama serve
    ```

2.  **Model**: Pull your desired model.

    Bash

    ```bash
    ollama pull llama3.1:8b
    ```

3.  **API Keys**: Set up environment variables for external services in your `.env` file.

* * * * *

Example Interactions
--------------------

Bash

```bash
You: What is the weather in Alexandria now?
Titan is thinking... 🧠
Titan: Weather in Alexandria: Clear sky, 28°C, Humidity: 65%

You: Search for the next F1 Grand Prix.
Titan is thinking... 🧠
Titan: Search results as of 2025-09-05 17:30:00:

1. F1 Grand Prix Schedule
URL: https://www.formula1.com/en/latest/article.f1-2024-schedule.3rMhQxT9p.html
Description: The next race on the Formula 1 calendar is the Italian Grand Prix in Monza on September 6-8.

You: What is the time in Cairo?
Titan is thinking... 🧠
Titan: The current time in Cairo is 2025-09-05 17:31:00

You: Where am I?
Titan is thinking... 🧠
Titan: Your current location: Alexandria, Alexandria Governorate, Egypt
```

* * * * *

Common Models
-------------

-   `llama3.1:8b` - Fast and efficient

-   `llama3.1:70b` - More capable but slower

-   `codellama:7b` - Optimized for coding

-   `mistral:7b` - Alternative model

* * * * *

Troubleshooting
---------------

### Connection Issues

-   **"Cannot connect to Ollama"**: Make sure Ollama is running with `ollama serve`.

-   **"Model not found"**: Pull the model with `ollama pull <model-name>`.

### API Key Issues

-   **"Search API key not configured"**: Set `SERPER_API_KEY` environment variable.

-   **"Weather API key not configured"**: Set `OPENWEATHERMAP_API_KEY` environment variable.

* * * * *

License
-------

MIT License - feel free to use and modify as needed.