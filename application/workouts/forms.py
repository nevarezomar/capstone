from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, DecimalField, DateTimeField
from wtforms.validators import DataRequired

class WorkoutFrom(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    lifting_movement = StringField('Lifting Movement', validators=[DataRequired()])
    type_of = SelectField('Type of Workout', choices=['Weight Lifting', 'Bike', 'Rower', 'Running'], validators=[DataRequired()])
    num_sets = IntegerField('Number of Sets')
    num_reps = IntegerField('Number of Reps')
    weight = DecimalField('Weight')
    rest_time = IntegerField('Rest time in Seconds')
    workout_date = DateTimeField('Enter Date of Workout')
    content = TextAreaField('Notes')
    submit = SubmitField('Post')

class Workout_ChoiceFrom(FlaskForm):
    type_of = SelectField('Type of Workout', choices=['Weight Lifting', 'Bike', 'Rower', 'Running'], validators=[DataRequired()])
    submit = SubmitField('Next')