from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Income(db.Model):
    __tablename__ = 'income'
    id = db.Column(db.Integer, primary_key=True)
    val = db.Column(db.Float, nullable=False)
    sender = db.Column(db.String(120), nullable=False)
    extra_info = db.Column(db.String(120), nullable=False)

    def __init__(self, val, sender, extra_info):
        self.val = val
        self.sender = sender
        self.extra_info = extra_info

    def __repr__(self):
        return f'{self.val}'


class Expenses(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    val = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(120), nullable=False)
    product_service = db.Column(db.String(120), nullable=False)

    def __init__(self, val, payment_method, product_service):
        self.val = val
        self.payment_method = payment_method
        self.product_service = product_service

    def __repr__(self):
        return f'{self.val}'
