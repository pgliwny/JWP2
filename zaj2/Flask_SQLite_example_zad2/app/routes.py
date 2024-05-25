from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Task

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_teacher():
    new_task = Task(name=request.get_json()['name'], subject=request.get_json()['subject'])
    db.session.add(new_task)
    db.session.commit()
    return '', 200


@app.route('/delete', methods=['GET', 'POST'])
def delete_teacher():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = Teacher.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('delete_teacher.html')