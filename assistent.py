#python personal assistent 
#created using simple if else statemants
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
from tkinter import *
import psutil





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ")   

    else:
        speak("Good Evening ")  

    speak("sir,I am Evin! how may i help you")       

def takeCommand():
    

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
        return query
        
   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
           

        elif 'open google' in query:
            speak("opening googel")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("opening stackoverfow")
            webbrowser.open("stackoverflow.com")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.in")
            speak("opening amazon")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif "battery percent" in query:
            battery = psutil.sensors_battery() 
  
            speak("Battery percentage is ",battery.percent)

        elif 'i am getting bored evin' in query: 
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
            if res.status_code == requests.codes.ok:
                talkToMe(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')
         



        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

    
        elif 'who created you' in query:
            speak("i was created by ,kshitij gavhane!")

     

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'I feeling very sweet after meeting with you but you are going! i am very sad'
            speak(ex_exit)
            exit()  

        elif 'open photoshop' in query:
            os.startfile("C:\Program Files\Adobe\Adobe Photoshop 2020\Photoshop.exe")

        elif 'open meet' in query:
            webbrowser.open("https://meet.google.com/landing?authuser=3")

        elif 'open mail inbox' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open hackerrank' in query:
            webbrowser.open("https://www.hackerrank.com/dashboard")


        elif 'thank you' in query:
            speak("Welcome Sir..it iS MY DUTY TO HELP YOU OUT")

        

        else:
            temp = query.replace(' ','+')
            g_url="https://www.google.com/search?q="    
            res_g = 'sorry! i cant understand but i search from internet to give your answer !'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)    




        
