from flask import render_template, url_for, flash, redirect, request
from application import application, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import User, Workout
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Omar Nevarez',
        'title': 'Workout 1',
        'content': 'First posted content',
        'date_posted': 'January 28, 2022'
    },
    {
        'author': 'Not Omar',
        'title': 'Workout 2',
        'content': 'Second posted content',
        'date_posted': 'January 29, 2022'
    }
]



@application.route("/")
@application.route("/home")
def home():
    return render_template('home.html', posts=posts)

@application.route("/about")
def about():
    return render_template('about.html', title='About')

@application.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created! Please login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@application.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@application.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@application.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')