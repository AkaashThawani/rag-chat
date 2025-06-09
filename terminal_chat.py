import os
import google.generativeai as genai
import pprint
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=key)

try:
    model = genai.GenerativeModel("gemini-2.0-flash")
except Exception as e:
    raise ValueError(f"Failed to get model: {e}")


def main():
    print("Welcome to the Terminal Chat with Gemini!")
    print("Type 'exit' to quit the chat.")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Exiting chat. Goodbye!")
            break

        try:
            response = model.generate_content(user_input)
            print(f"Gemini: {response.text}")
        except Exception as e:
            print(f"Error generating response: {e}")


if __name__ == "__main__":
    main()
