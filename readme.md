# Gemini Terminal Chat

A simple, interactive command-line chatbot that uses the Google Gemini API. This project allows you to have a direct, general-purpose conversation with a powerful language model right from your terminal.


*(Image: Example of the chatbot in action)*

## Features

- **Direct Conversation:** Chat directly with Google's Gemini models (`gemini-1.5-flash` by default).
- **Easy Setup:** Requires only Python and a single library.
- **Secure API Key Handling:** Uses a `.env` file to keep your API key safe and out of the source code.
- **Cross-Platform:** Works on Windows, macOS, and Linux.

## Prerequisites

Before you begin, ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python's package installer, usually included with Python)

You will also need a **Google Gemini API Key**.
1.  Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Sign in with your Google account.
3.  Click "**Create API key**" and copy the generated key.

## Installation

1.  **Clone the repository or download the files.**
    If you're using Git, clone the repository:
    ```bash
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```
    Otherwise, just create a folder and place the `terminal_chat.py` file inside it.

2.  **Install the required Python libraries.**
    Open your terminal in the project folder and run:
    ```bash
    pip install -r requirements.txt
    ```
    *(If you don't have a `requirements.txt` file, you can install the packages manually):*
    ```bash
    pip install google-generativeai python-dotenv
    ```

3.  **Set up your API Key.**
    - In the same project folder, create a new file named `.env`.
    - Open the `.env` file and add your Gemini API key in the following format:
      ```
      GEMINI_API_KEY="YOUR_API_KEY_HERE"
      ```
    - Replace `"YOUR_API_KEY_HERE"` with the key you copied from Google AI Studio. **Do not use quotes** inside the `.env` file.

    > **Important:** The `.env` file should never be committed to public version control (like GitHub). If you are using Git, create a `.gitignore` file and add `.env` to it.

## Usage

Once the installation and setup are complete, you can run the chatbot from your terminal.

1.  Navigate to the project directory.
2.  Run the following command:
    ```bash
    python terminal_chat.py
    ```
3.  The chat will start, and you will see a `You:` prompt. Type your message and press Enter to get a response from Gemini.

**Example Session:**
```
--- Welcome to Gemini Terminal Chat ---
Ask me anything! Type 'exit', 'quit', or 'bye' to end the chat.
---------------------------------------
You: Hello! Who are you?
Gemini: I am a large language model, trained by Google.
You: Can you write a short poem about code?
Gemini: Lines of logic, clean and bright,
       Solving problems, day and night.
       A bug appears, a moment's fight,
       Then sweet success, a pure delight.
You: exit
Gemini: Goodbye!
```

To stop the chat, simply type `exit`, `quit`, or `bye` and press Enter.

## Code Overview (`terminal_chat.py`)

- **`dotenv`**: This library is used at the start to load the `GEMINI_API_KEY` from your `.env` file into the environment.
- **`google.generativeai`**: This is the official Google AI Python SDK.
  - `genai.configure()`: Sets up the authentication using the API key.
  - `genai.GenerativeModel()`: Creates an instance of the chat model (e.g., `gemini-1.5-flash-latest`).
  - `model.generate_content()`: Sends the user's input to the Gemini API and retrieves the generated response.
- **Main Loop:** The `while True:` loop continuously prompts the user for input, sends it to the model, prints the response, and checks for exit commands.