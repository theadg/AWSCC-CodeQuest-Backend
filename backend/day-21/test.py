from flask import Flask, Blueprint

app = Flask(__name__)

from routes import mainBlueprint

app.register_blueprint(mainBlueprint)

if __name__ == '__main__':
    app.run()