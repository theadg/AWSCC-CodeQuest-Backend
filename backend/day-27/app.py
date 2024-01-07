from src import create_app
from src.routes import views
import logging

app = create_app()
# Set up logging
logging.basicConfig(level=logging.DEBUG)
app.register_blueprint(views)


if __name__ == "__main__":
    app.run(debug=True)