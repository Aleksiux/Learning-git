import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, surname, message):
        self.name = name
        self.surname = surname
        self.date = datetime.datetime.now().replace(microsecond=0)
        self.message = message

    def __repr__(self):
        return f'{self.name} {self.surname}, {self.date}\n{self.message}'
