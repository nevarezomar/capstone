from datetime import datetime
from application import db, login_manager, application
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    height = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    workouts = db.relationship('Workout', backref='member', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(application.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(application.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}, {self.email}, {self.image_file}')"

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    type_of = db.Column(db.String(60), nullable=False)
    lifting_movement = db.Column(db.String(60), nullable=False)
    weight = db.Column(db.Float, nullable=True)
    num_reps = db.Column(db.Integer, nullable=True)
    num_sets = db.Column(db.Integer, nullable=True)
    rest_time = db.Column(db.Integer, nullable=True)
    workout_date = db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Workout('{self.title}, {self.workout_date}')"