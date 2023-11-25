# URL-Shortener

URL Shortener with Python

This Python script enables users to shorten URLs using the pyshorteners library while validating the provided URLs using the validators module.
Features

    Validates user input to ensure a properly formatted URL.
    Shortens valid URLs using the TinyURL service through pyshorteners.
    Gracefully handles exit commands such as typing "exit" or "quit" or Ctrl C.

Prerequisites

    Python 3.x
    Install required libraries:

    bash

    pip install pyshorteners validators

Usage

    Clone this repository or download the script (shorten_url.py).
    Open a terminal or command prompt.
    Navigate to the directory containing shorten_url.py.
    Run the script:

    bash

    python shorten_url.py

    Follow the on-screen instructions to enter the URL you want to shorten. To exit, type "exit" or "quit".

Example

bash

$ python shorten_url.py
Enter the URL: [Enter your URL here]
Shortened URL: [Generated shortened URL]

Notes

    If an invalid URL is entered, the script prompts the user to enter a valid URL.
    Typing "exit" or "quit" or Ctrl C during the URL input prompt exits the script.
    The script uses pyshorteners for URL shortening and validators for URL validation.
