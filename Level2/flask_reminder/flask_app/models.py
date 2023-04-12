from Level2.flask_reminder.flask_app import db

helper_table = db.Table('helper',
                        db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
                        db.Column('lecture_id', db.Integer, db.ForeignKey('lecture.id')))


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    surname = db.Column('surname', db.String)
    lectures = db.relationship('Lecture', secondary=helper_table)


class Professor(db.Model):
    __tablename__ = 'professor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    surname = db.Column('surname', db.String)
    experience = db.Column('experience', db.Integer)
    lectures = db.relationship('Lecture')


class Lecture(db.Model):
    __tablename__ = 'lecture'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    students = db.relationship('Student', secondary=helper_table)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    professor = db.relationship('Professor')
