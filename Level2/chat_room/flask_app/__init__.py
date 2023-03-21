import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.app_context().push()

from Level2.chat_room.flask_app import routes
