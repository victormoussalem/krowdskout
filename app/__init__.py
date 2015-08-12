from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# setting up template directory
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static/app')

app = Flask(__name__, template_folder=ASSETS_DIR, static_folder=ASSETS_DIR)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models

if __name__ == '__main__':
    app.run(debug=True)
