from wtforms import StringField, SubmitField, PasswordField, EmailField
from flask_wtf import FlaskForm
from Level2.FlaskUsers.flask_users.models import Users
from wtforms.validators import DataRequired, ValidationError, EqualTo, Email
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from Level2.FlaskUsers.flask_users import app

class RegisterForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    first_name = StringField('First name', [DataRequired()])
    last_name = StringField('Last name', [DataRequired()])
    email = EmailField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    confirm_password = PasswordField('Confirm password', [EqualTo('password', 'Password do not match')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        username = Users.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError('This username is already taken. Choose another one')

    def validate_email(self, email):
        email = Users.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This email is already taken. Choose another one.')


class LoginForm(FlaskForm):
    email = EmailField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Login')


class UserUpdateForm(FlaskForm):
    username = StringField('Username', [DataRequired()])
    first_name = StringField('First name', [DataRequired()])
    last_name = StringField('Last name', [DataRequired()])
    email = StringField('Email', [DataRequired()])
    photo = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            username = Users.query.filter_by(username=username.data).first()
            if username:
                raise ValidationError('This username is already taken. Choose another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            email = Users.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('This email is already taken. Choose another one.')


class RequestChangePasswordForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    submit = SubmitField('Get')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no such email. Check what you wrote again.')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Renew password')