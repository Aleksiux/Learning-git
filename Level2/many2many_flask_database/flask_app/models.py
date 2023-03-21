from Level2.many2many_flask_database.flask_app import db

helper_table = db.Table('helper',
                        db.Column('parent_id', db.Integer, db.ForeignKey('parents.id')),
                        db.Column('child_id', db.Integer, db.ForeignKey('children.id')))


class Parent(db.Model):
    __tablename__ = 'parents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    surname = db.Column('surname', db.String)
    age = db.Column('age', db.Integer)
    children = db.relationship('Child', secondary=helper_table, backref='parents')


class Child(db.Model):
    __tablename__ = 'children'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    surname = db.Column('surname', db.String)
    age = db.Column('age', db.Integer)
