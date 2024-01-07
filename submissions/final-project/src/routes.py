from flask import Blueprint, render_template, redirect, url_for, request
from .model import Account
from . import db
import logging

views = Blueprint("views", __name__)

@views.route("/")
def index():
    accounts = Account.query.all()
    
    return render_template('index.html', accounts=accounts)

@views.route("/add", methods=['GET', 'POST'])
def store():
    if request.method == 'GET':
        return render_template('store.html')
    
    # Get Account Details
    website = request.form.get('website')
    email = request.form.get('email')
    password = request.form.get('password')

    # Create new Account
    newAccount = Account(
        website=website, 
        email=email, password=password)
    db.session.add(newAccount)
    db.session.commit()

    return redirect(url_for('views.index'))

@views.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    # Find the Account
    account = Account.query.get(id)

    if request.method == 'GET':
        return render_template('update.html', account=account)

    # Get Account Details
    website = request.form.get('website')
    email = request.form.get('email')
    password = request.form.get('password')

    # Save Account info   
    account.website = website
    account.email = email
    account.password = password
    db.session.commit()
    return redirect(url_for('views.index'))

@views.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    book = Account.query.get(id)
    if book:
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('views.index'))
    
    return ({"results": "error"})