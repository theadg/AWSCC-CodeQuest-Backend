from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home pagess!'

@app.route('/about')
def about():
    return 'This is the about page.'

@app.route('/contact')
def contact():
    return 'You can contact us at contact@example.com.'

@app.route('/posts/<string:postName>')
def show(postName):
    return (f"Post Name mo to pre {postName}")

if __name__ == '__main__':
    app.run()