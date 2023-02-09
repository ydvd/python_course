import pyglet
import speech_recognition as sr
from commands import Commander

running = True
r = sr.Recognizer()
cmd = Commander()

def playAudio(filename):
    # Tutorial goes over using pyaudio as he couldn't get pyglet to work 
    # but turns out pyglet is pretty easy so there we go
    file = pyglet.resource.media(filename)
    file.play()

def initSpeech():
    print("Listening...")
    playAudio('audio/start.mp3')

    with sr.Microphone() as source:
        audio = r.listen(source)

    playAudio('audio/end.mp3')

    command = ""

    try:
        command = r.recognize_google(audio)
        print(command)
        if command == "quit":
            running = False

        cmd.discover(command)
    except:
        print("Couldn't understand")
    

while running == True:
    initSpeech()