from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    name = StringField('Username:', [DataRequired(message='You need fill this field')])
    room_code = StringField('Room Code')
    submit_join = SubmitField('Join room')
    submit_create = SubmitField('Create room')


class MessagesForm(FlaskForm):
    message = StringField('Message')
