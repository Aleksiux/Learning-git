from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [Email(message='Wrong address.'), DataRequired()])
    body = TextAreaField('Your message', [DataRequired(),
                                          Length(min=10,
                                                 message='Way too short text')])
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    email = StringField('Email', [Email(message='Wrong address.'), DataRequired()])
    password = PasswordField('Password', validators=[Length(min=8, message='Way to less symbols You need atleast 8 '
                                                                           'symbols'), DataRequired(message='You need'
                                                                                                            ' to fill'
                                                                                                            ' this '
                                                                                                            'field')])
    address = StringField('Address', validators=[DataRequired(message='You need to fill this field'),
                                                 Length(min=4, message='Way to less symbols you need atleast 8')])
    address2 = StringField('Address2', validators=[DataRequired(message='You need to fill this field'),
                                                   Length(min=4, message='Way to less symbols you need atleast 8')])
    city = StringField('City', validators=[DataRequired(message='You need to fill this field'),
                                           Length(min=4, message='Way to less symbols you need atleast 8')])
    state = SelectField('State', choices=['Vilnius', 'Kaunas'])
    zip = StringField('Zip', validators=[DataRequired(message='You need to fill this field'),
                                         Length(max=7, min=7, message='It should be only 7 characters')])
    select = BooleanField('I love spam in emails:)))')
    submit = SubmitField('Submit')


class Yt_Downloader(FlaskForm):
    downloader = StringField('Write URL of YT link', [DataRequired()])
    submit = SubmitField('Download')
