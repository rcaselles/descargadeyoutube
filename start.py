import poplib
import smtplib
from email.mime.text import MIMEText
from tempfile import TemporaryFile

from gtts import gTTS
from playsound import playsound

import funcionesutiles
from funcionesutiles import buscalugar
import pychromecast

from funcionesutiles import buscavideo
from funcionesutiles import anadirportada
from voz import decir
# Establecemos conexion con el servidor smtp de gmail
"""mailServer = smtplib.SMTP('smtp.gmail.com',587)
mailServer.ehlo()
mailServer.starttls()
mailServer.ehlo()
mailServer.login("rcaselles98@gmail.com","")
mensaje = MIMEText("Este es el mensaje de prueba")
mensaje['From']="rcaselles98@gmail.com"
mensaje['To']="rcaselles98@gmail.com"
mensaje['Subject']="Tienes un correo"
mailServer.sendmail("rcaselles98@gmail.com",
                "rcaselles98@gmail.com",
                mensaje.as_string())
"""
"""m = poplib.POP3_SSL('pop.gmail.com',995)
m.user('rcaselles98@gmail.com')
m.pass_('')
numero = len(m.list()[1])
print(numero)"""
while True:
    prueba = input("Introduce la cancion que quieres buscar:")
    decir('He encontrado la cancion ' + str(prueba))
    buscavideo(str(prueba),True)


