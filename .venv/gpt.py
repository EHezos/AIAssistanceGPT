# pip install pyttsx3
# pip install SpeechRecognition
# pip install revChatGPT
# Toturial to setup chatgpt https://www.youtube.com/watch?v=0GXI9148dxg
# go to config.json to replace your token

import speech_recognition as sr
import pyttsx3
from revChatGPT.Unofficial import Chatbot
import json

def main():
    # Read config
    with open(".venv\config.json") as f:
        token = json.load(f)

    # Initialize Chatbot API
    api = Chatbot(token)

    r = sr.Recognizer()
    text_speech = pyttsx3.init()

    # Start conversation
    print("Bot: Hi how can I help you today!")
    text_speech.say("Hi how can I help you today?!")
    text_speech.runAndWait()

    while True:
        # Speech recognition
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Bot: Please say something...")
            text_speech.say("Please say Something!")
            text_speech.runAndWait()
            audio = r.listen(source)

            try:
                print("Recognizing...")
                text = r.recognize_google(audio)
                print("You: " + text)
                print("Please wait I am processing.....")

                # Send user's message to the chatbot and get response
                resp = api.ask(text)
                bot_response = resp['message']
                print("Bot: " + bot_response)

                # Text-to-speech for bot response
                text_speech.say(bot_response)
                text_speech.runAndWait()

                # Say oh no to quit xD
                if "oh no" in text:
                    text_speech.say("Thank you for using me")
                    text_speech.runAndWait()
                    break

            except Exception as e:
                if "OSError" in str(e):
                    print("Error: [WinError 6] The handle is invalid")
                else:
                    print("Error: " + str(e))
if __name__ == "__main__":
    main()
