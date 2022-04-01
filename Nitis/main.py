import sys
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from commands import Commander

running = True


def say(mytext):
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("pcSpeech.mp3")
    playsound('./pcSpeech.mp3')


def play_audio(filename):
    playsound(filename)


r = sr.Recognizer()

cmd = Commander()


def initSpeech():
    print("Listening...")

    play_audio("./Audio/1stsound.wav")

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    play_audio("./Audio/2ndsound.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
        print("your command:")
        print(command)
        if command not in ["nothing", "that's it"]:
            if command in ["quit", "exit", "bye", "goodbye"]:
                global running
                running = False
                say("see you soon, bhai.")
                return
            cmd.discover(command)
            if  "open" in command:
                running = False
                say("see you soon, bhai.")
                return
            if command not in ["what is your name", "what is my name", "I am great", "I am fine", "I am alright", "I am ok", "I am good"]:
                print("What will you like to know next bro?")
                say("what will you like to know next bro?")
        else:
            say("Alright then, say exit to quit")
        return
    except:
        print("Couldn't understand you")
        say("Couldn't understand you")


    #say(' You said: ' + command)


while running==True:
    initSpeech()
