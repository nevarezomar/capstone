import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


application = Flask(__name__)

application.config['SECRET_KEY'] = '9fe2cf6f218f9017cb0f237ec1621555'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
application.config['MAIL_SERVER'] = 'smtp.googlemail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
application.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(application)

from application import routes