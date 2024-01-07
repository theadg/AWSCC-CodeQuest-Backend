from flask import Blueprint

# this blueprint for routes can be in another file
mainBlueprint = Blueprint('main', __name__)

@mainBlueprint.route('/')
def home():
    return "Welcome to the home page"

@mainBlueprint.route('/about')
def about():
    return "Do you really work?"