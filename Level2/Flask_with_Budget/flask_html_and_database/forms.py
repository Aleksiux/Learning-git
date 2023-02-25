from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length


class IncomeForm(FlaskForm):
    val = DecimalField('Income', [DataRequired(message='You need fill this field')])
    sender = StringField('Sender', validators=[Length(min=8, message='Way to less symbols You need atleast 8 '
                                                                     'symbols'), DataRequired(message='You need'
                                                                                                      ' to fill'
                                                                                                      ' this '
                                                                                                      'field')])
    extra_info = StringField('Extra info',
                             validators=[Length(min=6, message='Way to less symbols You need atleast 6 '
                                                               'symbols'), DataRequired(message='You need'
                                                                                                ' to fill'
                                                                                                ' this '
                                                                                                'field')])
    submit = SubmitField('Submit')


class ExpensesForm(FlaskForm):
    val = DecimalField('Expenses', [DataRequired(message='You need fill this field')])
    payment_method = StringField('Payment method',
                                 validators=[Length(min=6, message='Way to less symbols You need atleast 6 '
                                                                   'symbols'), DataRequired(message='You need'
                                                                                                    ' to fill'
                                                                                                    ' this '
                                                                                                    'field')])
    product_service = StringField('Product service',
                                  validators=[Length(min=6, message='Way to less symbols You need atleast 6 '
                                                                    'symbols'), DataRequired(message='You need'
                                                                                                     ' to fill'
                                                                                                     ' this '
                                                                                                     'field')])
    submit = SubmitField('Submit')
