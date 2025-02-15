from .. import db
from datetime import datetime

class StudySession(db.Model):
    __tablename__ = 'study_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    study_activity_id = db.Column(db.Integer, db.ForeignKey('study_activities.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    group = db.relationship('Group', back_populates='study_sessions')
    study_activity = db.relationship('StudyActivity', back_populates='study_sessions')
    word_review_items = db.relationship('WordReviewItem', back_populates='study_session')

    @property
    def correct_count(self):
        return sum(1 for item in self.word_review_items if item.correct)

    @property
    def total_reviews(self):
        return len(self.word_review_items) 