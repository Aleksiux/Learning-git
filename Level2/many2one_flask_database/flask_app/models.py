from Level2.many2one_flask_database.flask_app import db


class Parent(db.Model):
    __tablename__ = 'parent'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    surname = db.Column('surname', db.String)
    age = db.Column('age', db.Integer)
    child_id = db.Column(db.Integer, db.ForeignKey('child.id'))
    child = db.relationship('Child')


class Child(db.Model):
    __tablename__ = 'child'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    surname = db.Column('surname', db.String)
    age = db.Column('age', db.Integer)
