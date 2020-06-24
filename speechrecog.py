import speech_recognition as sr

from os import path

Ad_file = path.join(path.dirname(path.realpath(__file__)), "You're Always Loved.mp3")

r = sr.Recognizer()

with sr.AudioFile(Ad_file) as source:
    audio = sr.record(source)
    
    try:
        text = sr.recognize_google(audio)
        print('You said: {}'.format(text))  
    except:
        print('Not recognizedd')
        