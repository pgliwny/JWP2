from app import db
import datetime

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    subject = db.Column(db.String(120), unique=True, nullable=False)
    time =  db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return '<Teatcher %r>' % self.name