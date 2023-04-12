from wtforms import StringField, FloatField, SubmitField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class ItemForm(FlaskForm):
    item_name = StringField('Item name', [DataRequired()])
    price = FloatField('Price', [DataRequired()])
    quantity = IntegerField('Quantity', [DataRequired()])
    submit = SubmitField('Press me')
