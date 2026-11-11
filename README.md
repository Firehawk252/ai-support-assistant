# AI Support Assistant
A Python-based application that uses a locally running AI model to analyze IT support issues and provide troubleshooting guidance. Users can describe technical problems, interact with the AI, and save conversations to revisit later.

## Features
- Issue Analysis: Understand the user's description of a technical problem.
- Troubleshooting Guidance: Provide step-by-step troubleshooting recommendations.
- Conversation History: Maintain conversation context during a session.
- Save Conversations: Save conversations locally using JSON.
- Load Conversations: Restore previously saved conversations and continue troubleshooting.
- Conversation Management: Rename and delete saved conversations.
- Input Validation: Handle invalid selections, missing files, and malformed conversation data.

## Technologies
- Python
- Ollama
- Llama 3.2
- JSON
- OS module (file management)

## Requirements
- Python 3
- Ollama
- Llama 3.2 model

## Setup
- Install Python
- Install Ollama
- Download the Llama 3.2 model
  - `ollama pull llama3.2`
- Install the Python Ollama library
  - `pip install ollama`
- Run the application
  - `python main.py`

## Available Commands
| Command | Description |
|---|---|
| `new` | Start a new conversation |
| `save` | Save the current conversation |
| `load` | Load a saved conversation |
| `rename` | Rename a saved conversation |
| `delete` | Delete a saved conversation |
| `history` | Display conversation history |
| `help` | Display available commands |
| `exit` | Close the application |

## Future Improvements
- Issue categorization
- Priority assessment
- Knowledge base of common IT issues and solutions
