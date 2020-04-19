import os
import subprocess

from gtts import gTTS
from playsound import playsound
def play(audio_file_path):
    subprocess.call(["ffplay", "-nodisp", "-autoexit", audio_file_path])
def decir(texto):
    tts = gTTS(text=str(texto), lang='es-es', slow=False)
    tts.save('hello.mp3')
    playsound('hello.mp3')
    os.remove('hello.mp3')