from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

application = Flask(__name__)

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
mail = Mail(application)

login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

application.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
application.config['MAIL_SERVER'] = 'smtp.googlemail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
application.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')

from application.users.routes import users
from application.workouts.routes import workouts
from application.main.routes import main
from application.errors.handlers import errors

application.register_blueprint(users)
application.register_blueprint(workouts)
application.register_blueprint(main)
application.register_blueprint(errors)
