from openai import OpenAI
import time
import webbrowser
import json
import platform
import os
from datetime import datetime
from gtts import gTTS

# Initialize conversation and engine
conversation_history = []

API_KEY = "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"
API_KEY = "ENTER YOUR API KEY HERE"


def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("voice.mp3")
        os.system("mpv --really-quiet voice.mp3")
        os.remove("voice.mp3")
    except Exception as e:
        print(f"[Speech Error] {e}")


def save_history():
    with open("chat_history.json", "w") as file:
        json.dump(conversation_history, file, indent=4)

def show_history():
    if os.path.exists("chat_history.json"):
        with open("chat_history.json", "r") as file:
            history = json.load(file)
            print("\n--- Chat History ---")
            for i, msg in enumerate(history, 1):
                role = msg["role"].capitalize()
                content = msg["content"].strip()
                timestamp = msg.get("timestamp", "N/A")
                print(f"{i}. [{timestamp}] {role}: {content}\n")
    else:
        print("\n[!] No chat history found.")

def clear_history():
    if os.path.exists("chat_history.json"):
        os.remove("chat_history.json")
        print("[+] Chat history cleared.")
        speak("Chat history has been cleared.")
    else:
        print("[!] No chat history to clear.")

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def help_menu():
    help_commands = {
        "clear": "Clears the terminal screen",
        "open youtube": "Opens YouTube in browser",
        "open google": "Opens Google in browser",
        "open wikipedia": "Opens Wikipedia in browser",
        "open instagram": "Opens Instagram in browser",
        "open facebook": "Opens Facebook in browser",
        "open reddit": "Opens Reddit in browser",
        "bye / exit / good bye": "Ends the assistant session"
    }
    print("\n--- Available Voice Commands ---")
    for cmd, desc in help_commands.items():
        print(f"{cmd:<20} - {desc}")

def ai_assistant(prompt):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY,
    )
    conversation_history.append({
        "role": "user",
        "content": prompt,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick:free",
        messages=conversation_history
    )
    assistant_reply = completion.choices[0].message.content
    conversation_history.append({
        "role": "assistant",
        "content": assistant_reply,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    return assistant_reply

def main():

    speak("Welcome To Shinrai. Your Personal AI Assistant!!, You can ask me anything or say help.")
    conversation_history.append({
        "role": "system",
        "content": "New session started",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    command_urls = {
        "open youtube": "https://www.youtube.com/",
        "open instagram": "https://www.instagram.com/",
        "open facebook": "https://www.facebook.com/",
        "open reddit": "https://www.reddit.com/",
        "open wikipedia": "https://www.wikipedia.org/"
    }

    
    running = True

    while running:
        try:
            prompt = input("\nYou: ").strip()    
            
            if not prompt:
                continue

            time.sleep(1)

            if prompt.lower() in command_urls:
                url = command_urls[prompt.lower()]
                site = prompt.split()[-1].capitalize()
                speak(f"Opening {site}")
                print(f"\nAI: Opening {site}...")
                webbrowser.open(url)

            elif prompt.lower() == "help":
                help_menu()
                speak("Here are the available commands.")

            elif prompt.lower() == "clear":
                clear_screen()
                continue

            elif any(keyword in prompt.lower() for keyword in ["search", "google"]):
                for word in ["search", "google", "for"]:
                    prompt = prompt.lower().replace(word, "")
                query = prompt.strip()
                if query:
                    speak(f"Searching Google for {query}")
                    print(f"\nAI: Searching Google for {query}")
                    webbrowser.open(f"https://www.google.com/search?q={query.replace(' ', '+')}")
                else:
                    speak("What should I search?")
                continue

            elif prompt.lower() in ["bye", "exit", "good bye"]:
                speak("Goodbye!")
                running = False
                continue

            else:
                response = ai_assistant(prompt)
                print(f"\nAI: {response}")
                speak(response)

        except KeyboardInterrupt:
            print("\n[!] Program interrupted by user.")
            break

        except Exception as e:
            print(f"[Error] : {e}")
            speak("Something went wrong.")
            break

    save_history()

if __name__ == '__main__':
    while True:
        print("--- Python AI Assistant ---")
        print("1) Start Assistant")
        print("2) Check History")
        print("3) Clear chat History")
        print("4) Exit")

        try:
            choice = int(input("\nEnter your choice (1-4): "))
        except ValueError:
            print("Enter a valid option please !!")
            continue
        except KeyboardInterrupt:
            print("")
            break

        if choice == 1:
            clear_screen()

            main()

        elif choice == 2:
            show_history()

        elif choice == 3:
            clear_history()

        elif choice == 4:
            conversation_history.append({
                "role": "system",
                "content": "Session Ended",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            break

        else:
            print("Please select a valid option.")
