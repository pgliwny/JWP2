from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    subject = db.Column(db.String(120), unique=False, nullable=False)
    time = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<Teacher %r>' % self.name
