from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from Level2.one2many_flask_database.flask_app.models import Child, Parent


def child_query():
    return Child.query


def parent_query():
    return Parent.query


class ParentForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    surname = StringField('Surname', [DataRequired()])
    age = IntegerField('Age', [DataRequired()])
    children = QuerySelectMultipleField(
        query_factory=child_query, allow_blank=True, get_label='name', get_pk=lambda obj: str(obj))
    submit = SubmitField('Submit')


class ChildForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    surname = StringField('Surname', [DataRequired()])
    age = IntegerField('Age', [DataRequired()])
    parents = QuerySelectField(
        query_factory=parent_query(), allow_blank=True, get_label='name', get_pk=lambda obj: str(obj))
    submit = SubmitField('Submit')
