import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
     engine.say(audio)
     engine.runAndWait()


def wishMe():
    hour = int (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<17:
        speak("Good Afternoon")

    else:
        speak("Good Evening") 

    speak("I am your assistant. How may I help you")       

def takeCommand():


    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing........")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say that again.....")
        return "None"       
    return query

def sendmail(content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(gmailaddress,password)
        server.sendmail(gmailaddress,mailto,content)
        server.close()



if __name__ == "__main__":
        wishMe()
        while True:
              query = takeCommand().lower()



              if 'wikipedia' in query:
                  speak("Searching Wikipedia")
                  query = query.replace("wikipedia","")
                  results = wikipedia.summary(query,sentences= 2)
                  speak("According to wikipedia")
                  print(results)
                  speak(results)
              elif 'open youtube' in query:
                  speak("Playing Youtube")
                  webbrowser.open("youtube.com")
              elif 'open google' in query:
                  speak("Processing")
                  webbrowser.open("google.com")   
              elif 'play music' in query:
                  speak("Playing music")
                  music_dir = 'D:\\Music'
                  songs = os.listdir(music_dir)
                  print(songs)
                  os.startfile(os.path.join(music_dir,songs[0]))
              elif 'the time' in query:
                  strTime = datetime.datetime.now().strftime("%H:%M:%S")
                  speak(f"Sir,the time is {strTime}")             
              elif 'open code' in query:
                  speak("Opening Code")
                  codePath = "C:\\Users\\Vignesh K S\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                  os.startfile(codePath)
              elif 'open pycharm' in query:
                  speak("opening pycharm")
                  py="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.2\\bin\\pycharm64.exe"    
                  os.startfile(py)
              elif 'open googlechrome' in query:
                  google = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                  os.startfile(google)
              elif 'open Movie' in query:
                  speak("Opening Movie folder")
                  movie_dir='D://Movie'
                  movies=os.listdir(movie_dir)
                  print(movies)
                  os.startfile(os.path.join(movie_dir,movies[0]))
              elif 'send email' in query:
                  try:
                      speak("Your gmail address and password")
                      gmailaddress=input("enter the address")
                      password=input("enter the password")
                      speak("enter the receiver address")
                      mailto=input("enter the email address of receiver")
                      speak("what should i say")
                      content=takeCommand()
                      sendmail(content)
                      speak("Email has been sent")
                  except Exception as e:
                      print(e)
                      speak("Sorry Mail not sent")

              elif 'hello' in query:
                   speak("Hi")
              elif 'how are you' in query:
                   speak("I am fine...Feel free to ask anything")
              elif 'What is your name' in query:
                   speak(" My name is Enigma")