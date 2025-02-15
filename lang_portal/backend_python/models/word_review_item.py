from .. import db
from datetime import datetime

class WordReviewItem(db.Model):
    __tablename__ = 'word_review_items'
    
    id = db.Column(db.Integer, primary_key=True)
    word_id = db.Column(db.Integer, db.ForeignKey('words.id'), nullable=False)
    study_session_id = db.Column(db.Integer, db.ForeignKey('study_sessions.id'), nullable=False)
    correct = db.Column(db.Boolean, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    word = db.relationship('Word', back_populates='review_items')
    study_session = db.relationship('StudySession', back_populates='word_review_items') 