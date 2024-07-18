from .db import db   # This is the database object that we will use to interact with the database

class User(db.Model):
    __tablename__='users'
    UserID = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(50), index=True, nullable = False)
    Email = db.Column(db.String(120), nullable = False)

class TextCreated(db.Model):
    __tablename__='text_created'
    TextCreatedID = db.Column(db.Integer, primary_key=True)
    UserID = db.Column(db.Integer, db.ForeignKey('users.UserID'), nullable = False)
    MetaDataUsed = db.Column(db.String(255), nullable = False)

class BookData(db.Model):
    __tablename__='book_data'
    BookDataID = db.Column(db.Integer, primary_key=True)
    Authors = db.Column(db.String(255), nullable = False)
    Title = db.Column(db.String(255), nullable = False)
    Year = db.Column(db.Integer, nullable = False)
    Subjects = db.Column(db.String(255), nullable = False)
    Bookshelves = db.Column(db.String(255), nullable = False)
    Copyright = db.Column(db.Boolean, nullable = False)

class LineFetched(db.Model):
    __tablename__='line_fetched'
    LineFetchedID = db.Column(db.Integer, primary_key=True)
    BookDataID = db.Column(db.Integer, db.ForeignKey('book_data.BookDataID'), nullable = False)
    Excerpt = db.Column(db.Text, nullable = False)

class LineStamped(db.Model):
    __tablename__='line_stamped'
    LineStampedID = db.Column(db.Integer, primary_key=True)
    TextCreatedID = db.Column(db.Integer, db.ForeignKey('text_created.TextCreatedID'), nullable = False)
    LineFetchedID = db.Column(db.Integer, db.ForeignKey('line_fetched.LineFetchedID'), nullable = False)
