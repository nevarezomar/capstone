from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from application import db
from application.models import Workout
from application.workouts.forms import (LiftingWorkoutForm, RunningWorkoutForm, 
                                        RowingWorkoutForm, BikingWorkoutForm, Workout_ChoiceForm)

workouts = Blueprint('workouts', __name__)

@workouts.route("/workout/workout_choice", methods=['GET', 'POST'])
@login_required
def workout_choice():
    form = Workout_ChoiceForm()
    if form.validate_on_submit():
        type_of = form.type_of.data
        if type_of=='Weight Lifting':
            return redirect(url_for('workouts.new_lifting_workout'))
        elif type_of=='Running':
            return redirect(url_for('workouts.new_running_workout'))
        elif type_of=='Rowing':
            return redirect(url_for('workouts.new_rowing_workout'))
        elif type_of=='Biking':
            return redirect(url_for('workouts.new_biking_workout'))
    return render_template('workout_choice.html', form=form, title='Workout Type')

    
@workouts.route("/workout/new_lifting", methods=['GET', 'POST'])
@login_required
def new_lifting_workout():
    form = LiftingWorkoutForm()
    if form.validate_on_submit():
        workout = Workout(title=form.title.data, lifting_movement=form.lifting_movement.data, 
            type_of='Weight Lifting', num_sets=form.num_sets.data, num_reps=form.num_sets.data, weight=form.weight.data, 
            rest_time=form.rest_time.data, workout_date=form.workout_date.data, content=form.content.data, member=current_user)
        db.session.add(workout)
        db.session.commit()
        flash('Your workout has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_lifting_workout.html', title='New Weight Lifting Workout', form=form, legend='New Weight Lifting Workout')

@workouts.route("/workout/new_running", methods=['GET', 'POST'])
@login_required
def new_running_workout():
    form = RunningWorkoutForm()
    if form.validate_on_submit():
        pace = form.total_duration.data / form.total_distance.data
        workout = Workout(title=form.title.data,type_of='Running', 
        total_distance=form.total_distance.data, total_duration=form.total_duration.data,
        workout_date=form.workout_date.data, pace=pace, content=form.content.data, member=current_user)
        db.session.add(workout)
        db.session.commit()
        flash('Your workout has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_running_workout.html', title='New Running Workout', form=form, legend='New Running Workout')

@workouts.route("/workout/new_rowing", methods=['GET', 'POST'])
@login_required
def new_rowing_workout():
    form = RowingWorkoutForm()
    if form.validate_on_submit():
        pace = (form.total_duration.data / form.total_distance.data) * 500
        total_strokes = int(form.stroke_rate.data*form.total_duration.data)
        workout = Workout(title=form.title.data, type_of='Rowing', 
        total_distance=form.total_distance.data, total_duration=form.total_duration.data,
        workout_date=form.workout_date.data, stroke_rate=form.stroke_rate.data, pace=pace,
        total_strokes=total_strokes, content=form.content.data, member=current_user)
        db.session.add(workout)
        db.session.commit()
        flash('Your workout has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_rowing_workout.html', title='New Rowing Workout', form=form, legend='New Rowing Workout')

@workouts.route("/workout/new_biking", methods=['GET', 'POST'])
@login_required
def new_biking_workout():
    form = BikingWorkoutForm()
    if form.validate_on_submit():
        pace = form.total_duration.data / form.total_distance.data
        workout = Workout(title=form.title.data,type_of='Biking', 
        total_distance=form.total_distance.data, total_duration=form.total_duration.data,
        workout_date=form.workout_date.data, content=form.content.data, pace=pace, member=current_user)
        db.session.add(workout)
        db.session.commit()
        flash('Your workout has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_biking_workout.html', title='New Biking Workout', form=form, legend='New Biking Workout')

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
    type_of = workout.type_of
    if type_of == 'Weight Lifting':
        form = LiftingWorkoutForm()
        if form.validate_on_submit():
            workout.title = form.title.data
            workout.lifting_movement = form.lifting_movement.data
            workout.type_of = form.type_of.data
            workout.num_sets = form.num_sets.data
            workout.num_reps = form.num_reps.data
            workout.weight = form.weight.data
            workout.rest_time = form.rest_time.data
            workout.content = form.content.data
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
            form.content.data = workout.content
        return render_template('new_lifting_workout.html', title='Update Workout', form=form, legend='Update Workout')
    elif type_of == 'Running':
        form = RunningWorkoutForm()
        if form.validate_on_submit():
            workout.title = form.title.data
            workout.type_of = form.type_of.data
            workout.total_distance = form.total_distance.data
            workout.total_duration = form.total_duration.data
            pace = form.total_duration.data / form.total_distance.data
            workout.pace = pace
            workout.content = form.content.data
            db.session.commit()
            flash('Post has been updated!', 'success')
            return redirect(url_for('workouts.workout', workout_id=workout.id))
        elif request.method == 'GET':
            form.title.data = workout.title
            form.type_of.data = workout.type_of
            form.total_distance.data = workout.total_distance
            form.total_duration.data = workout.total_duration
            form.content.data = workout.content
        return render_template('new_running_workout.html', title='Update Workout', form=form, legend='Update Workout')
    elif type_of == 'Rowing':
        form = RowingWorkoutForm()
        if form.validate_on_submit():
            workout.title = form.title.data
            workout.type_of = form.type_of.data
            workout.total_distance = form.total_distance.data
            workout.total_duration = form.total_duration.data
            workout.stroke_rate = form.stroke_rate.data
            pace = (form.total_duration.data / form.total_distance.data) * 500
            total_strokes = int(form.stroke_rate.data*form.total_duration.data)
            workout.pace = pace
            workout.total_strokes = total_strokes
            workout.content = form.content.data
            db.session.commit()
            flash('Post has been updated!', 'success')
            return redirect(url_for('workouts.workout', workout_id=workout.id))
        elif request.method == 'GET':
            form.title.data = workout.title
            form.type_of.data = workout.type_of
            form.total_distance.data = workout.total_distance
            form.total_duration.data = workout.total_duration
            form.stroke_rate.data = workout.stroke_rate
            form.content.data = workout.content
        return render_template('new_rowing_workout.html', title='Update Workout', form=form, legend='Update Workout')
    elif type_of == 'Biking':
        form = BikingWorkoutForm()
        if form.validate_on_submit():
            pace = form.total_duration.data / form.total_distance.data
            workout.pace = pace
            workout.title = form.title.data
            workout.type_of = form.type_of.data
            workout.total_distance = form.total_distance.data
            workout.total_duration = form.total_duration.data
            workout.content = form.content.data
            db.session.commit()
            flash('Post has been updated!', 'success')
            return redirect(url_for('workouts.workout', workout_id=workout.id))
        elif request.method == 'GET':
            form.title.data = workout.title
            form.type_of.data = workout.type_of
            form.total_distance.data = workout.total_distance
            form.total_duration.data = workout.total_duration
            form.content.data = workout.content
        return render_template('new_biking_workout.html', title='Update Workout', form=form, legend='Update Workout')

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