import random
import pyttsx3
import speech_recognition as sr

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognising your voice.......")
        query=r.recognize_google(audio,language='en.in')
        print("user said:\n"+ str(query))
    except Exception as e:
        print(e)
        print("Could not recognise your voice\nPlease speak again")
    return query
def game(comp,you):
    if comp==you:
        return None
    elif comp=='rock':
        if you=='scissors':
            return False
        elif you=='paper':
            return True
    elif comp=='paper':
        if you=='rock':
            return False
        elif you=='scissors':
            return True
    elif comp=='scissors':
        if you=='paper':
            return False
        elif you=='rock':
            return True
        
def result():
    speak("You choosed" +you)
    speak("and computer choosed"+comp)
    print("You choosed" +you)
    print("and computer choosed"+comp)


print("****Welcome to Rock Paper Scissors Game****")
speak("Welcome to Rock Paper Scissors Game")

while True:

    randno=random.randint(1,9)

    if randno>=1 and randno<=3:
        comp='rock'
    elif randno>=4 and randno<=6:
        comp='paper'
    elif randno>=7 and randno<=9:
        comp='scissors'
        
     #Taking input from user
    print("Your turn: Speak your choices from")
    speak("Please speak your choice")
    print("1> Rock")
    print("2> Paper")
    print("3> Scissors")
    print("4> Stop")

    you = takeCommand()
    if 'stop' in you:
        break
    elif you!='rock' and you!='paper' and you!='scissors':
        speak("Invalid choice")
        print("Invalid choice")
    elif 'rock' or 'paper' or 'scissors' in you:
        a=game(comp,you)
        if a==None:
            result()
            print("Draw")
            speak("Draw")
        if a==False:
            result()
            print("lost")
            speak("lost")
        if a==True:
            result()
            print("won")
            speak("won")