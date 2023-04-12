from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from Level2.many2one_flask_database.flask_app.models import Child


def child_query():
    return Child.query


class ParentForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    surname = StringField('Surname', [DataRequired()])
    age = IntegerField('Age', [DataRequired()])
    children = QuerySelectField(query_factory=child_query, allow_blank=True, get_label='name',
                                get_pk=lambda obj: str(obj))
    submit = SubmitField('Submit')


class ChildForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    surname = StringField('Surname', [DataRequired()])
    age = IntegerField('Age', [DataRequired()])
    submit = SubmitField('Submit')
