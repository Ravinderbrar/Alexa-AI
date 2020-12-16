import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser
import pywhatkit
import datetime
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# voices[0].id -> male voice
# voices[1].id -> female voice


# changing default browser
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))


def speak(stuff_to_speak):
    ''' to speak any thing '''
    engine.say(stuff_to_speak)
    engine.runAndWait()

def takeCommand():
    ''' this function takes command'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        query.lower()
        if 'alexa' in query:
            query = query.replace('alexa','')
            print(query)
            
        
    
    except:
        return "None"

    
    return query

def listen_less():
    ''' this function takes command'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        query.lower()
        query = query.replace('alexa','')
        print(query)
            
            
        
    
    except:
        return "None"

    
    return query





if __name__ == "__main__":
    speak(" moring ")
    while True:

        query = takeCommand().lower()


        if 'quit' in query or 'sign out' in query:
            speak(" Signing out Sir")
            exit()

        elif 'youtube' in query:
            speak(" opening youtube")
            webbrowser.get('chrome').open("youtube.com")
        
        elif 'play' in query:
            query = query.replace('alexa','')
            query = query.replace('play','')
            speak(f" playing {query}")
            pywhatkit.playonyt(query)
        
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f' Sir it is {time}')
        
        elif 'whatsapp' in query:
            speak(' Opening whatsapp')
            webbrowser.get('chrome').open('https://web.whatsapp.com/')

        elif 'google meet' in query:
            speak(' opening google meet')
            webbrowser.get('chrome').open('meet.google.com')
        
        elif 'instagram' in query:
            speak(' opening instagram')
            webbrowser.get('chrome').open('instagram.com')
        
        elif 'facebook' in query:
            speak(' opening facebook')
            webbrowser.get('chrome').open('facebook.com')

        # elif 'vs code' in query or 'code' in query:
        #     parent_dir = "D:/"
        #     speak( ' project name please')
        #     project_name = listen_less().lower()
        #     path = os.path.join(parent_dir,project_name)
            
        #     check_project = os.path.isdir(path)
        #     if(check_project == False):
        #         new_path = f"{parent_dir}//{project_name}"
        #         make_folder = os.mkdir(new_path)
        #         # reaching terminal
        #         os.system("code .")
                

    
                
                

            

            

