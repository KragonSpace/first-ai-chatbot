import numpy as np
# speech recognition - google api
import speech_recognition as sr
# convert text to speech
from gtts import gTTS
import os
# respond log
import datetime

# Beginning of the AI
class ChatBot():
    def __init__(self, name):
        print("----- starting up", name, "-----")
        self.name = name

    # Using Google APIs
    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
            print("listening...")
            audio = recognizer.listen(mic)
        try:
            self.text = recognizer.recognize_google(audio)
            print("me --> ", self.text)
        except:
            print("me -->  ERROR")
    
    # Activate the bot by saying 'Hello Dev' or 'Hey Dev'
    def wake_up(self, text):
        return True if self.name in text.lower() else False

    # text to speech
    @staticmethod
    def text_to_speech(text):
        print("AI --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("start res.mp3")  #if you have a macbook->afplay or for windows use->start
        os.remove("res.mp3")
    
    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')
    #and run the script after adding the above function to the AI class



# Execute the AI
if __name__ == "__main__":
    # Create a chatbot
    ai = ChatBot(name="Dev")
    # Convert Speech to Text
    while True:
        ai.speech_to_text()
        
        # Wake up
        if ai.wake_up(ai.text) is True:
            res = "Hello I am Dev the AI, what can I do for you?"
        # Do any action
        elif "time" in ai.text:
            res = ai.action_time()
        # respond politely
        elif any(i in ai.text for i in ['thank', 'thanks']):
            res = np.random.choice(
                ["Your're welcom!", "anytime!", "no porblem!",
                 "cool!", "I'm here if you need me!", "pace out!"]
            )
        # Chatbot say to respond the human's order
        ai.text_to_speech(res)

