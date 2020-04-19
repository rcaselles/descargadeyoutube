from io import StringIO
import json
import subprocess
import tempfile
import urllib.request
import youtube_dl
import urllib.parse

from PIL.Image import Image
from google_images_download import google_images_download
from gtts import gTTS
from tempfile import TemporaryFile
from playsound import playsound
import os
import pychromecast
import eyed3
import urllib
import requests
from io import StringIO
#play del Pydub
import time

def play(audio_file_path):
    subprocess.call(["ffplay", "-nodisp", "-autoexit", audio_file_path])
def anadirportada(nombre, directoriocan):
    headers = {'apikey': '1ee66c20-819c-11ea-b98d-af42afd01274'}

    params = (
        ("q", nombre + " Caratula"),
        ("tbm", "isch"),
        ("device", "desktop"),
        ("location", "Spain"),
    );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params);
    img_data = requests.get(response.json()['image_results'][0]['sourceUrl']).content
    with open('/media/rcaselles/45EE630C5E0B75A4/' + nombre + '.jpg', 'wb') as handler:
        handler.write(img_data)


    audiofile = eyed3.load(directoriocan)
    if (audiofile.tag == None):
        audiofile.initTag()

    audiofile.tag.images.set(3, open('/media/rcaselles/45EE630C5E0B75A4/' + nombre + '.jpg', 'rb').read(), 'image/jpeg')

    audiofile.tag.save()

    print(response.json()['image_results'][1]['sourceUrl'])


def download(link, nombre, streaming):
    ydl_opts = {
        'outtmpl': '/media/rcaselles/45EE630C5E0B75A4/' + nombre + '.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    anadirportada(nombre,'/media/rcaselles/45EE630C5E0B75A4/' + nombre + '.mp3')
    chromecasts = pychromecast.get_chromecasts()
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == "Nosaltres four")
    cast.wait()
    mc = cast.media_controller
    mc.play_media('http://192.168.1.99:8000/' + nombre + '.mp3', 'audio/mp3')
    mc.block_until_active()
    mc.play()

    playsound('/media/rcaselles/45EE630C5E0B75A4/' + nombre + '.mp3')
    if streaming == True:
        os.remove('/media/rcaselles/45EE630C5E0B75A4/' + nombre + '.mp3')


def buscavideo(str, streaming):
    actual = time.time()

    if "serafin" in str:
        return exit()
    x = " "
    url = "http://youtube-scrape.herokuapp.com/api/search?q=" + urllib.parse.quote(str) + "&page=1"
    respuesta = urllib.request.urlopen(url)

    data = json.loads(respuesta.read())
    print(data['results'][0]['video']['title'])
    x = data['results'][0]['video']['title']
    print(data['results'][0]['video']['url']);
    download(data['results'][0]['video']['url'], x, streaming)
    final = time.time()
    print(final-actual)
    return


def buscalugar(str):
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=" + urllib.parse.quote(str) + "&inputtype=textquery&fields=formatted_address,name&key=AIzaSyAeXqYwuFmYgK9CL5Sfgv6TzB0SscOn2wU"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    test = json.dumps(data)
    if "serafin" in str:
        return exit()
    if "ZERO" not in test:
        datos2 = data["candidates"]
        print(datos2[0]["name"])
        print(datos2[0]["formatted_address"])
    return
