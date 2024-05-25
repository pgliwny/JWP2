from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User
from app.models import Teacher

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/teachers')
def teacher_index():
    teachers = Teacher.query.all()
    return render_template('teacher_index.html', teachers=teachers)

@app.route('/teachers/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        if name and subject:
            new_teacher = Teacher(name=name, subject=subject)
            db.session.add(new_teacher)
            db.session.commit()
            return redirect(url_for('teacher_index'))
    return render_template('add_user.html')

@app.route('/teachers/delete', methods=['GET', 'POST'])
def delete_teacher():
    if request.method == 'POST':
        teacher_id = request.form['teacher_id']
        teacher = Teacher.query.get(teacher_id)
        if teacher:
            db.session.delete(teacher)
            db.session.commit()
            return redirect(url_for('teacher_index'))
    return render_template('delete_user.html')

@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if username and email:
            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('delete_user.html')
