from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<string:pageName>/<int:number>')
def home(pageName,number):
    title = "My Web App"
    user = "Alice"
    return render_template('index.html', title=pageName, user=number)