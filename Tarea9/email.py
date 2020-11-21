#!/usr/bin/python

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse
import smtplib
import json


descripcion = """ Modo de uso:
    sendmail.py -to 'Destinatario' -subj 'Asunto' -msj 'Mensaje' -atch 'Archivos adjuntos'"""
parser = argparse.ArgumentParser(description='emails sendings', epilog=descripcion,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-to", type=str, metavar='Destino', dest="to",
                    help="correo al que sera enviado el mensaje", required=True)
parser.add_argument("-subj", type=str, metavar='Asunto', dest="subj",
                    help="Agregar un asunto", required=True)
parser.add_argument("-msj", type=str, metavar='Mensaje', dest="msj",
                    help="Agregar mensaje", required=True)
parser.add_argument("-atch", type=str, metavar='Archivos', dest="atch",
                    help="Archivos adjuntos")
parameters = parser.parse_args()


data = {}
with open('pass.json') as f:
    data = json.load(f)
msg = MIMEMultipart()
message = parameters.msj

msg['From'] = data['user']
msg['To'] = parameters.to
msg['Subject'] = parameters.subj
msg.attach(MIMEText(message, 'plain'))

server = smtplib.SMTP(data['server'])
server.starttls()
server.login(data['user'], data['pass'])
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()

print("Se a enviado correctamente el correo de %s:" % (msg['To']))
