import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {name} sir")
    
    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon {name} sir")
    
    else:
        speak(f"Good Evening {name} sir")
    
    speak(f"I am Jarvis sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(emailID, content):
    # speak("Enter your mail ID: ")
    # senderEmail = input()
    senderEmail = "globalgroup850@gmail.com"
    
    # speak("Enter your mail password: ")
    # password = input()
    password = "Aggarwal@1810"
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(f"{senderEmail}, {password}")
    server.send(f"{senderEmail}, {emailID}, {content}")
    server.close()

if __name__ == "__main__":
    print("Tell me your name")
    name = takeCommand()
    
    wishMe()
    while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com/")
        
        elif "open google" in query:
            webbrowser.open("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com/")

        elif "play music" in query:
            music_dir = "D:\\Videos"
            songs = os.listdir(music_dir)
            play = random.randint(1, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[play]))
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")
        
        elif "open code" in query:
            codePath = "C:\\Users\\manav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open whatsapp" in query:
            whatsPath = "C:\\Users\\manav\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsPath)

        elif "send a mail" in query:
            # print("Please enter mail id you want to send a mail: ")
            # speak("Please enter mail id you want to send a mail: ")
            # emailID = input()
            emailID = "manav85068@gmail.com"
            
            try:
                speak("Enter your Message\n")
                content = input()
                sendEmail(emailID, content)
                speak("Email has been sent!")
            
            except Exception as e:
                speak(f"Sorry sir, I am not able to send this email")
        
        elif "quit" in query:
            exit()