from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

application = Flask(__name__)

application.config['SECRET_KEY'] = '9fe2cf6f218f9017cb0f237ec1621555'

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
def hello():
    return render_template('home.html', posts=posts)

@application.route("/about")
def about():
    return render_template('about.html', title='About')

@application.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@application.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    application.run(debug = True)