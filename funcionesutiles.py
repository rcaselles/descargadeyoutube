import json
import urllib.request
import youtube_dl
import urllib.parse
from gtts import gTTS
from tempfile import TemporaryFile
from playsound import playsound
import os
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

    playsound('/media/rcaselles/45EE630C5E0B75A4/' + nombre + '.mp3')
    if streaming == True:
        os.remove('/media/rcaselles/45EE630C5E0B75A4/' + nombre + '.mp3')


def buscavideo(str, streaming):
    if "serafin" in str:
        return exit()
    x = " "
    url = "http://youtube-scrape.herokuapp.com/api/search?q=" + urllib.parse.quote(str) + "&page=1"
    respuesta = urllib.request.urlopen(url)

    data = json.loads(respuesta.read())
    print(data['results'][0]['video']['title'])
    x = data['results'][0]['video']['title']
    print(data['results'][0]['video']['url']);
    download( data['results'][0]['video']['url'], x,streaming)
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