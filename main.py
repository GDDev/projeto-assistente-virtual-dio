from gtts import gTTS
import speech_recognition as sr
import os
from datetime import datetime
import playsound
import pyjokes
import webbrowser
from IPython.display import Audio

def get_audio():
    language = 'pt-BR'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio, language='pt-BR')
            print(said)
        except sr.UnknownValueError:
            speak('Me desculpe, não sei como responder à isso.', language)
        except sr.RequestError:
            speak('Serviço não reconhecido.', language)
    return said.lower()

def speak(text, language):
    tts = gTTS(text=text, lang=language)
    filename = 'voice.mp3'
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)


def textToAudio(transform):
    toTransform = transform
    language = 'pt-BR'

    gtts_object = gTTS(text=toTransform,
                       lang=language,
                       slow=False)

    speak('Texto transformado em áudio com sucesso!', language)
    gtts_object.save('./gtts.wav')
    Audio('./gtts.wav')

def respond(text):
    try:
        language = 'pt-BR'
        print(text)
        if 'youtube' in text:
            speak('O que você gostaria de assistir?', language)
            keyword = get_audio()
            if keyword != '':
                speak(f"Abrindo {keyword} no YouTube", language)
                url = f"https://www.youtube.com/results?search_query={keyword}"
                webbrowser.get().open(url)
        elif 'piada' in text:
            language = 'en'
            speak(pyjokes.get_joke(), language)
        elif 'horas' in text:
            strTime = datetime.today().strftime("%H:%M %p")
            print(strTime)
            speak(strTime, language)
        elif 'áudio' in text:
            speak('Transformando texto em áudio', language)
            transform = 'Alô'
            textToAudio(transform)
        elif 'esquece' in text:
            speak('Okay, até a próxima!', language)
    except Exception:
        pass

hearing = True
while hearing:
    print('Ouvindo...')
    text = get_audio()
    respond(text)
    hearing = False
