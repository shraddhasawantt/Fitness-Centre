
# coding: utf-8

# In[ ]:


import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb


engine=pyttsx3.init()

def speak(audio):
 engine.say(audio)
 engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("the current time is")
    speak(Time)

def date_():
    day=datetime.datetime.now().day
    month=datetime.datetime.now().month
    year=datetime.datetime.now().year
    speak("the date today is")
    speak(day)
    speak(month)
    speak(year)
    

def wishme():
    speak(" hello how are you today, i am your gym assistant")
    time_()
    date_()

    hour=datetime.datetime.now().hour

    if hour>=5 and hour<12:
        speak("gooooood morning its a fresh day to begin workout ")
    elif hour>=12 and hour<19:
        speak("its afternoon lets get active now")
    elif hour>=19 and hour<24:
        speak("good evening lets get the workout started and finish off the day")
    else:
        speak("goodnight for now but tommorow the work begins")

    speak("i did my work here")



        


def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)


    try:
        print("recognizing.....")
        query= r.recognize_google(audio,language="en-US")
        print(query)

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"

    return query

    
if __name__=="__main__":
    

    while True:
        query= TakeCommand().lower()

        if "time" in query:
            time_()
        elif " assistant" in query:
            wishme()
        elif "date" in query:
            date_()
        elif 'facts' in query:
            speak("searching....")
            query=query.replace("wikipedia",'')
            result=wikipedia.summary(query,sentences=4)
            speak("according to the gym assistant")
            print(result)
            speak(result)
        elif 'workout' in query:
            speak("searching....")
            query=query.replace("wikipedia",'')
            result=wikipedia.summary(query,sentences=4)
            speak("according to the gym assistant")
            print(result)
            speak(result)
    

        elif 'quit' in query:
            speak("  bye     bye   ")
            exit()


# In[ ]:




