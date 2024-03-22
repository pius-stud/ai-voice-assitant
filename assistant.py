from gtts import gTTS
from speech_recognition import Microphone, Recognizer
import playsound


import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

lang = 'en' # 'it' for italian, 'en' for english

def talk(text):
    speech = gTTS(text = text, lang=lang, slow=False, tld="com", )
    speech.save("welcome1.mp3")
    playsound.playsound("welcome1.mp3")


def take_command():
    r = Recognizer()

    with Microphone() as source:
        print('Listening...')
        audio = r.listen(source)
        request = r.recognize_google(audio, language = 'en-EN')
        request = request.lower()

    return request
