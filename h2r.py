import speech_recognition as sr
from gtts import gTTS 
import os

voice=""

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio, language = 'en', show_all = True)
            print(text)
            if text == "stop" or text == "exit":
                break
            voice = voice + str(text)
        except:
            print("say something...") 

hr=gTTS(text = voice, lang='en', slow = False)
hr.save("1.wav")