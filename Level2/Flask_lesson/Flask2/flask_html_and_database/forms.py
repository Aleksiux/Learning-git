from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    name = StringField('Name', validators=[Length(min=8, message='Way to less symbols You need atleast 8 '
                                                                 'symbols'), DataRequired(message='You need'
                                                                                                  ' to fill'
                                                                                                  ' this '
                                                                                                  'field')])
    surname = StringField('Surname', validators=[Length(min=8, message='Way to less symbols You need atleast 8 '
                                                                       'symbols'), DataRequired(message='You need'
                                                                                                        ' to fill'
                                                                                                        ' this '
                                                                                                        'field')])
    message = TextAreaField('Your message', [DataRequired(),
                                             Length(min=10,
                                                    message='Way too short text')])
    submit = SubmitField('Submit')
