from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from application import db
from application.models import Workout
from application.workouts.forms import WorkoutFrom, Workout_ChoiceFrom

workouts = Blueprint('workouts', __name__)

@workouts.route("/workout/workout_choice", methods=['GET', 'POST'])
@login_required
def workout_choice():
    form = Workout_ChoiceFrom()
    if form.validate_on_submit():
        type_of = form.type_of.data
        print("inside validation form")
        return render_template('new_workout.html', title='New Workout', form=form, legend='New Workout', type_of=type_of)
    print("inside validation form")
    return render_template('workout_choice.html', form=form, title='Workout Type')

    


@workouts.route("/workout/new", methods=['GET', 'POST'])
@login_required
def new_workout():
    form = WorkoutFrom()
    if form.validate_on_submit():
        workout = Workout(title=form.title.data, lifting_movement = form.lifting_movement.data, 
            type_of = form.type_of.data, num_sets=form.num_sets.data, num_reps=form.num_sets.data, weight=form.weight.data, 
            rest_time=form.rest_time.data, workout_date=form.workout_date.data, content=form.content.data, member=current_user)
        db.session.add(workout)
        db.session.commit()
        flash('Your workout has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_workout.html', title='New Workout', form=form, legend='New Workout')

@workouts.route("/workout/<int:workout_id>")
@login_required
def workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    return render_template('workout.html', title=workout.title, workout=workout)

@workouts.route("/workout/<int:workout_id>/update", methods=['GET', 'POST'])
@login_required
def update_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    if workout.member != current_user:
        abort(403)
    form = WorkoutFrom()
    if form.validate_on_submit():
        workout.title = form.title.data
        workout.lifting_movement = form.lifting_movement.data
        workout.type_of = form.type_of.data
        workout.num_sets = form.num_sets.data
        workout.num_reps = form.num_reps.data
        workout.weight = form.weight.data
        workout.rest_time = form.rest_time.data
        db.session.commit()
        flash('Post has been updated!', 'success')
        return redirect(url_for('workouts.workout', workout_id=workout.id))
    elif request.method == 'GET':
        form.title.data = workout.title
        form.lifting_movement.data = workout.lifting_movement
        form.type_of.data = workout.type_of
        form.num_sets.data = workout.num_sets
        form.num_reps.data = workout.num_reps
        form.weight.data = workout.weight
        form.rest_time.data = workout.rest_time
    return render_template('new_workout.html', title='Update Workout', form=form, legend='Update Workout') 

@workouts.route("/workout/<int:workout_id>/delete", methods=['POST'])
@login_required
def delete_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    if workout.member != current_user:
        abort(403)
    db.session.delete(workout)
    db.session.commit()
    flash('Your workout has been deleted!', 'success')
    return redirect(url_for('main.home'))