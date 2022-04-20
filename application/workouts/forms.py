from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, IntegerField, DecimalField, DateTimeField
from wtforms.validators import DataRequired

class LiftingWorkoutForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    lifting_movement = StringField('Lifting Movement', validators=[DataRequired()])
    type_of = SelectField('Type of Workout', choices=['Weight Lifting', 'Biking', 'Rowing', 'Running'])
    num_sets = IntegerField('Number of Sets')
    num_reps = IntegerField('Number of Reps')
    weight = DecimalField('Weight')
    rest_time = IntegerField('Rest time in Seconds')
    workout_date = DateTimeField('Enter Date of Workout')
    content = TextAreaField('Notes')
    submit = SubmitField('Post')

class RowingWorkoutForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    type_of = SelectField('Type of Workout', choices=['Weight Lifting', 'Biking', 'Rowing', 'Running'])
    total_duration = DecimalField('Duration (Minutes)', validators=[DataRequired()])
    stroke_rate = DecimalField('Average Number of Strokes per Minute', validators=[DataRequired()])
    total_distance = DecimalField('Total Distance (Meters)', validators=[DataRequired()])
    workout_date = DateTimeField('Enter Date of Workout')
    content = TextAreaField('Notes')
    submit = SubmitField('Post')

class RunningWorkoutForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    type_of = SelectField('Type of Workout', choices=['Weight Lifting', 'Biking', 'Rowing', 'Running'])
    total_distance = DecimalField('Total Distance (Miles)', validators=[DataRequired()])
    total_duration = DecimalField('Duration (Minutes)', validators=[DataRequired()])
    workout_date = DateTimeField('Enter Date of Workout')
    content = TextAreaField('Notes')
    submit = SubmitField('Post')

class BikingWorkoutForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    type_of = SelectField('Type of Workout', choices=['Weight Lifting', 'Biking', 'Rowing', 'Running'])
    total_distance = DecimalField('Total Distance (Miles)', validators=[DataRequired()])
    total_duration = DecimalField('Duration (Minutes)', validators=[DataRequired()])
    workout_date = DateTimeField('Enter Date of Workout')
    content = TextAreaField('Notes')
    submit = SubmitField('Post')

class Workout_ChoiceForm(FlaskForm):
    type_of = SelectField('Type of Workout', choices=['Weight Lifting', 'Biking', 'Rowing', 'Running'])
    submit = SubmitField('Next')