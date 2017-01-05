# Import flask and template operators
from flask import Flask, render_template
from flask_cors import CORS
from app.chat import runChat

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)
CORS(app)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (events)
from app.events.models import *
from app.trades.models import *
from app.users.models import *
from app.events.views import events
from app.users.views import users
from app.trades.views import trades

# Register blueprint(s)
app.register_blueprint(events, url_prefix='/api/events')
app.register_blueprint(users, url_prefix='/api/hr')
app.register_blueprint(trades, url_prefix='/api/trades')

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

