from flask import render_template, request, Blueprint
from flask_login import current_user, login_required
from application.models import Workout, User
from application import db

main = Blueprint('main', __name__)

@main.route("/")
def landing_page():
    return render_template('landing_page.html')

@main.route("/home")
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    workouts = Workout.query.filter_by(user_id=current_user.id).order_by(Workout.workout_date.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', workouts=workouts)

@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/leaderboard")
def leaderboard():
    return render_template('leaderboard.html', title='Leaderboard')