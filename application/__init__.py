from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


application = Flask(__name__)

application.config['SECRET_KEY'] = '9fe2cf6f218f9017cb0f237ec1621555'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(application)

from application import routes