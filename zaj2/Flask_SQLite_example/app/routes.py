from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Teacher

@app.route('/')
def index():
    teachers = Teacher.query.all()
    return render_template('index.html', teachers=teachers)

@app.route('/add', methods=['GET', 'POST'])
def add_teacher():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        if name and subject:
            new_user = Teacher(name=name, subject=subject)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('add_teacher.html')

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