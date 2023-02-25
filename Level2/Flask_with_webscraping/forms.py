from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class GpuSearch(FlaskForm):
    gpu_name = StringField('GPU name', [DataRequired(message='You need fill this field')])
    submit = SubmitField('Search')
