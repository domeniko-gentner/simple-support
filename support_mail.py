import smtplib
import json
from collections import namedtuple
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def get_config():
    f = open("./credentials.json")
    data = f.read()
    return json.loads(data,
                      object_hook=lambda d:
                      namedtuple('X', d.keys())(*d.values()))


def get_template(sender: str, subject: str, room: str, body: str):
    f = open("templates/mail.tpl")
    mail = f.read()
    mail = mail.replace("sender", sender)
    mail = mail.replace("subject", subject)
    mail = mail.replace("room", room)
    mail = mail.replace("body", body)
    return mail


def send_mail(sender: str, subject: str, room: str, body: str):
    cred = get_config()
    server = smtplib.SMTP_SSL(cred.server, cred.port)
    server.ehlo()
    server.login(cred.username, cred.password)

    msg = MIMEMultipart()
    msg["subject"] = subject
    msg["From"] = cred.username
    msg["To"] = cred.username
    body = get_template(sender, subject, room, body)

    msg.attach(MIMEText(body, 'plain'))
    server.sendmail(cred.username, cred.username, msg.as_string())
    server.quit()
