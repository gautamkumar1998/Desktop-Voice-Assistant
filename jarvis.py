import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[0].id)
# engine.SetProperty('voice',voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning Sir, Have a nice day")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon sir")
    else:
        speak("Good Evening sir")

    speak("I am Jarvis Sir. Please tell me how may I help you")

#   For Recognition of voice

def takeCommand():
    # It takes microphone input and gives us string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_thresold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        
    except Exception as e:
        print(e)
        print("Say that again please......")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kgauti31@gmail.com','gautamkumar@1998')
    server.sendmail('gk509050@gmail.com', to, content)
    server.close()
if __name__ == '__main__':
    speak("Gautam is a good boy")
    wishMe()
    while True:
    # if query == True:
        query = takeCommand().lower()

        
        # Logic for execution tasks based on query
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'play music' in query:
            music_dir = 'D:\\Non\\sectoral\\songs\\Favroite songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir, the time is:", strTime)
            
        elif 'open code' in query:
            codePath = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'mail to Gautam' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "gk509050@gmail.com"
                sendEmail(to, content)
                speak("Email is sent...")
            except Exception as e:
                print(e)
                speak("Sorry Sir...I am not able to send email at this moment..")
                            
