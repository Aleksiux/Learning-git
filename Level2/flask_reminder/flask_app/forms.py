from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectMultipleField, QuerySelectField
from Level2.flask_reminder.flask_app.models import Lecture, Student, Professor


def students_query():
    return Student.query.all


def teachers_query():
    return Professor.query.all


def lectures_query():
    return Lecture.query.all


def name_and_surname(data_query):
    return f'{data_query.name} {data_query.surname}'


class StudentForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    surname = StringField('Surname', [DataRequired()])
    lectures = QuerySelectMultipleField(query_factory=lectures_query(), allow_blank=True,
                                        get_label='name',
                                        get_pk=lambda obj: str(obj))
    submit = SubmitField('Submit')


class TeacherForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    surname = StringField('Surname', [DataRequired()])
    experience = IntegerField('Experience', [DataRequired()])
    lectures = QuerySelectMultipleField(query_factory=lectures_query(), allow_blank=True,
                                        get_label='name',
                                        get_pk=lambda obj: str(obj))
    submit = SubmitField('Submit')


class LecturesForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    professor = QuerySelectField(query_factory=Professor.query.all, allow_blank=True, get_label=name_and_surname,
                                 get_pk=lambda obj: str(obj))
    students = QuerySelectMultipleField(query_factory=Student.query.all, allow_blank=True, get_label=name_and_surname,
                                        get_pk=lambda obj: str(obj))
    submit = SubmitField('Submit')
