import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from ollama import chat     # offline Models I am currently using llama3.2:1b (Super fast for quick answering)
from ollama import ChatResponse
from gtts import gTTS
import pygame
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "30941296a79b4ffa8aa88e92bc00073a"

def speak(text):
    engine.say(text)
    engine.runAndWait()


def speak(text):
    tts = gTTS('hello')
    tts.save('temp.mp3')
    pygame.mixer.init()                    # start the sound system
    pygame.mixer.music.load("temp.mp3")    # change to your file name/path
    pygame.mixer.music.play()              # start playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)            

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
def AIprocess(command):
    response : ChatResponse = chat(model = "llama3.2:1b" , messages = [
        {
            "role" : "System",
            "content" : "You are a virtual assistant named 'jarvis' skilled in general tasks like Alexa and google cloud . Give short responses please"
        },
        {
            "role" : "User",
            "content" : command
        },
    ])

    return response['message']['content']


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                print(article['title'])
    else:
        # Let llama3.2:3b model(offline) handle the request : 
        output = AIprocess(c.lower())
        print(output)


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))

            