from flask import Flask

app = Flask(__name__)
baseUrl = '/api/tasks'
# Sample data (list of tasks)
tasks = []

from notes import notesBp
    
# Register routes for notes
app.register_blueprint(notesBp, url_prefix='/api/tasks')

if __name__ == '__main__':
    app.run()