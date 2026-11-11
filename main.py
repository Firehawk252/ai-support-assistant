# AI Support Assistant is an application where users describe an IT problem, and an AI assistant analyzes
# the issue and provides troubleshooting guidance.
# Firehawk252 11/10/2026
# v.1.0

# Requirements:
#   Import the ollama library
#   Create a function called ask_ai()
#   Accept a user's question as an argument
#   Send that question to the llama3.2 model
#   Display the AI's response

# Ollama's Python library uses ollama.chat() to send messages to a model

import ollama
import os
import json

def ask_ai(messages):

    try:
        response = ollama.chat(
            model="llama3.2",
            messages = messages
        )

        answer = response["message"]["content"]
        messages.append({"role": "assistant", "content": answer})
        print(answer)
    except Exception as error:
        print(error)
        print("AI service is unavailable. Please try again.")

def create_messages():
    messages = [
        {"role": "system", "content": "You are an IT support technician. Provide clear, step-by-step troubleshooting"
                                      "instructions. Start with basic checks before advanced troubleshooting."
                                      "Ask clarifying questions when necessary. Avoid recommending changes that"
                                      "could disrupt production systems. Never assume a network problem is DNS-related"
                                      "without evidence. Explain what a command does before recommending it."
                                      "Never recommend disruptive commands without warning the user."},
    ]
    return messages

# This function will allow users to save their current troubleshooting conversation to a text file
def save_conversation(messages, filename):
    if filename == "":
        print("Filename cannot be empty.")
        return

    elif os.path.exists(filename + ".txt"):
        print("A conversation with that filename already exists.")
        return

    with open(filename + ".txt", "w") as file:
        json.dump(messages, file, indent=4)

    print("Conversation saved!")

# This function will let users view the conversation so far without having to scroll back through the terminal
def display_history(messages):
    if len(messages) == 1:
        print("No conversation history yet.")
    else:
        for message in messages:
            if message["role"] != "system":
                print(message["role"] + ": " + message["content"])

# This function will let users open and resume previously saved conversations from the application
def load_conversation(filename):
    try:
        with open(filename + ".txt", "r") as file:
            messages = json.load(file)
            if not isinstance(messages, list):
                print("Invalid conversation file.")
                return None
            for message in messages:
                if not isinstance(message, dict) or "role" not in message or "content" not in message:
                    print("Invalid conversation file.")
                    return None
            return messages
    except FileNotFoundError:
        print("File not found.")
        return None
    except json.JSONDecodeError:
        print("Unable to load conversation.")
        return None

# This function will display the list of saved conversations
def list_saved_conversations():
    saved_files = []

    for filename in os.listdir():
        if filename.endswith(".txt"):
            saved_files.append(filename)

    for index, filename in enumerate(saved_files, start=1):
        print(str(index) + ". " + filename)

    return saved_files

# This function lets users delete a saved conversation by filename
def delete_conversation(filename):
    if os.path.exists(filename + ".txt"):
        os.remove(filename + ".txt")
        print("Conversation deleted!")
    else:
        print("File not found.")

# This function allows users to rename an existing saved conversation without opening or changing its contents
def rename_conversation(filename, new_filename):
    if os.path.exists(filename + ".txt"):
        os.rename(filename + ".txt", new_filename + ".txt")
        print("Conversation renamed!")
    else:
        print("File not found.")

def main():
    print("=================================")
    print("     AI IT Support Assistant")
    print("=================================")

    messages = create_messages()

    while True:
        question = input("You: \n")
        if question == "":
            print("Please enter an IT issue.")
            continue
        elif question.lower() == "exit":
            print("Goodbye!")
            break
        elif question.lower() == "new":
            print("Starting a new conversation!")
            messages = create_messages()
            continue
        elif question.lower() == "save":
            filename = input("Enter a filename: ")
            save_conversation(messages, filename)
            continue
        elif question.lower() == "load":
            saved_files = list_saved_conversations()
            if len(saved_files) == 0:
                print("No saved conversations found.")
                continue
            try:
                choice = int(input("Select a conversation: "))
                if choice < 1 or choice > len(saved_files):
                    print("Invalid choice.")
                    continue
            except ValueError:
                print("Invalid choice.")
                continue
            filename = saved_files[choice - 1]
            loaded_messages = load_conversation(filename[:-4])

            if loaded_messages is not None:
                messages = loaded_messages
                print("Conversation loaded!")
            continue
        elif question.lower() == "delete":
            saved_files = list_saved_conversations()
            if len(saved_files) == 0:
                print("No saved conversations found.")
                continue
            try:
                choice = int(input("Select a conversation to delete: "))
                if choice < 1 or choice > len(saved_files):
                    print("Invalid choice.")
                    continue
            except ValueError:
                print("Invalid choice.")
                continue
            filename = saved_files[choice - 1]
            print("Deleting conversation " + filename)
            confirm = input("Are you sure you want to delete this conversation? (yes/no): ").lower()
            if confirm == "yes":
                delete_conversation(filename[:-4])
            elif confirm == "no":
                print("Deletion cancelled.")
            else:
                print("Invalid response. Please enter yes or no.")
            continue
        elif question.lower() == "rename":
            saved_files = list_saved_conversations()
            if len(saved_files) == 0:
                print("No saved conversations found.")
                continue
            try:
                choice = int(input("Select a conversation to rename: "))
                if choice < 1 or choice > len(saved_files):
                    print("Invalid choice.")
                    continue
            except ValueError:
                print("Invalid choice.")
                continue
            filename = saved_files[choice - 1]
            new_filename = input("Enter a new filename: ")
            if new_filename == "":
                print("New filename cannot be empty.")
                continue
            elif os.path.exists(new_filename + ".txt"):
                print("A conversation with that filename already exists.")
                continue
            rename_conversation(filename[:-4], new_filename)
            continue

        elif question.lower() == "history":
            display_history(messages)
            continue
        elif question.lower() == "help":
            print("'new' will start a new conversation")
            print("'exit' will close the application")
            print("'save' will save the conversation")
            print("'load' will load the saved conversation")
            print("'delete' will delete a saved conversation")
            print("'rename' will rename a saved conversation")
            print("'history' will display the conversation so far")
            print("'help' will display available commands")
            continue
        messages.append({"role": "user", "content": question})
        ask_ai(messages)

if __name__ == "__main__":
    main()
