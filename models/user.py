from models import db
from datetime import datetime
from flask_login import UserMixin


# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    bio = db.Column(db.String(250), nullable=True)
    interests = db.relationship('Interest', backref='user', lazy=True)
