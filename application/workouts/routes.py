from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from application import db
from application.models import Workout
from application.workouts.forms import PostFrom

workouts = Blueprint('workouts', __name__)

@workouts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostFrom()
    if form.validate_on_submit():
        post = Workout(title=form.title.data, content=form.content.data, member=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('new_post.html', title='New Post', form=form, legend='New Post')

@workouts.route("/post/<int:post_id>")
@login_required
def post(post_id):
    post = Workout.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@workouts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Workout.query.get_or_404(post_id)
    if post.member != current_user:
        abort(403)
    form = PostFrom()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Post has been updated!', 'success')
        return redirect(url_for('workouts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('new_post.html', title='Update Post', form=form, legend='Update Post') 

@workouts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Workout.query.get_or_404(post_id)
    if post.member != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))