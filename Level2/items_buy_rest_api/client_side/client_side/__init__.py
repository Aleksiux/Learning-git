from flask import Flask
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

from Level2.items_buy_rest_api.client_side.client_side import routes
