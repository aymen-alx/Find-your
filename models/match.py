from models import db
from datetime import datetime


# Match model
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    matched_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)