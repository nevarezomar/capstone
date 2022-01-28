from flask import Flask

application = Flask(__name__)

@application.route("/")
@application.route("/home")
def hello():
    return "<h1>Hello Home!</h1>"

@application.route("/about")
def about():
    return "<h1>About Page!</h1>"

if __name__ == '__main__':
    application.run(debug = True)