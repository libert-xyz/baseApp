from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
#app.config.from_envvar('YOURAPPLICATION_SETTINGS')

db = SQLAlchemy(app)

from . import views, models
