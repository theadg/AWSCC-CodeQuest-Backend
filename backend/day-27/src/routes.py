from flask import Blueprint, render_template, redirect, url_for, request
from .model import Book
from . import db
import logging


views = Blueprint("views", __name__)

@views.route("/")
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)

@views.route("/add", methods=["POST"])
def add_book():
    author = request.form.get('author')
    title = request.form.get('title')
    published_year = request.form.get('published_year')
    new_book = Book(title=title, author=author, published_year=published_year)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('views.home'))


@views.route("/<int:id>", methods=["GET"])
def show(id):
    book = Book.query.get(id)
    return render_template('update.html', book=book)

@views.route("/update/<id>", methods=["POST"])
def update_book(id):
    # get data from form
    author = request.form.get('author')
    title = request.form.get('title')
    published_year = request.form.get('published_year')

    # updates
    book = Book.query.get(id)
    book.author = author
    book.title = title
    book.published_year = published_year
    db.session.commit()
    return redirect(url_for('views.home'))


@views.route("/delete/<id>", methods=["POST"])
def delete_book(id):
    book = Book.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return ({"results": "success"})
    return ({"results": "error"})