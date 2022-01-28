from flask import Flask, render_template, url_for

application = Flask(__name__)

posts = [
    {
        'author': 'Omar Nevarez',
        'title': 'Blog Post 1',
        'content': 'First posted content',
        'date_posted': 'January 28, 2022'
    },
    {
        'author': 'Not Omar',
        'title': 'Blog Post 2',
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

if __name__ == '__main__':
    application.run(debug = True)