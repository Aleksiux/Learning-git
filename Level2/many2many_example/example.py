helper_table = db.Table('helper',
                        db.Column('book_id', db.Integer, db.ForeignKey('books.id')),
                        db.Column('author_id', db.Integer, db.ForeignKey('authors.id')))


class Book(db.Model):

    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    publisher_id = db.Column(db.Integer, db.ForeignKey('publishers.id'))
    authors = db.relationship('Author', secondary=helper_table, backref='books')

    def __init__(self, title, publisher_id):
        self.title = title
        self.publisher_id = publisher_id

    def __repr__(self):
        return self.title


class Publisher(db.Model):

    __tablename__ = 'publishers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    books = db.relationship('Book', backref='publisher')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Author(db.Model):

    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150))
    lname = db.Column(db.String(300))

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'{self.fname} {self.lname}'