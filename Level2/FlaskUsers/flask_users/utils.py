import os
import secrets
from PIL import Image
from flask import url_for
import random
import string

from Level2.FlaskUsers.flask_users import app
from email.message import EmailMessage
import smtplib


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static', 'profile_pictures', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    sender = 'zerogravity5656@gmail.com'
    token = user.get_reset_token()
    msg = f'''If you want to reset password press on the link:
    {url_for('reset_password', token=token, _external=True)}
    If you did not pressed reset password just ignore this letter and password won't be changed.
    '''
    email_sender = EmailMessage()
    email_sender['From'] = sender
    email_sender['To'] = user.email
    email_sender['Subject'] = 'Password recovery'
    email_sender.set_content(msg)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(sender, 'eqhzrzupofncdygu')
    smtp.sendmail(sender, user.email, email_sender.as_string())
    smtp.quit()


rooms = {}


def generate_unique_code(length):
    while True:
        letters = string.ascii_uppercase
        room_code = ''.join(random.choice(letters) for _ in range(length))
        if room_code not in rooms:
            break
    return room_code
