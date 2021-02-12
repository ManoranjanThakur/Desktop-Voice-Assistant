import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')

engine.setProperty('voice' , voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour<12:
        speak("Good Morning Manoranjan")
    elif hour >=12 and hour<18:
        speak("Good Afternoon Manoranjan")
    else:
        speak("Good Evening Manoranjan")

    speak("I am your voice assistant , How may I help you?")

def takeCommand():
    """
    It takes microphone input from user and returns string output
    """

    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query} \n")
    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Write your email id and password
    server.login('myemail', 'password')
    server.sendemail('tosendemail', 'password')
    server.close()
    

if __name__ == "__main__" :
    wishMe()
    if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("youtube.com")
        elif 'open google' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("stackoverflow.com")
        elif 'linkedin profile' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://www.linkedin.com/in/manoranjan-kumar-thakur-2697851b0/")
        elif 'github profile' in query:
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("https://github.com/ManoranjanThakur")
        elif 'play naruto' in query:
            music_dir = 'C:\\Users\\HP\\Desktop\\Python\\python projects\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Sir The time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to ankit' in query:
            try:
                speak("What should i say")
                content= takeCommand()
                to = "ankit.nkit@gmail.com"
                sendEmail(to , content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir , I'm not able to send this email")
        