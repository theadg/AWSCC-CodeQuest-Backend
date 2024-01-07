from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_books.db'
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    published_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}-{self.author}>'

# db.create_all()

# new_book = Books(title="To Kill a Mockingbird", author="Harper Lee", published_year=1960)
# db.session.add(new_book)
# db.session.commit()

# books = Books.query.all()
