from .. import db
from datetime import datetime

# Define the association table at module level
word_groups = db.Table('word_groups',
    db.Column('word_id', db.Integer, db.ForeignKey('words.id'), primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True)
)

class Word(db.Model):
    __tablename__ = 'words'
    
    id = db.Column(db.Integer, primary_key=True)
    characters = db.Column(db.String(100), nullable=False)
    pinyin = db.Column(db.String(100), nullable=False)
    english = db.Column(db.String(100), nullable=False)
    parts = db.Column(db.ARRAY(db.String), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Use the association table defined above
    groups = db.relationship('Group', secondary=word_groups)
    review_items = db.relationship('WordReviewItem', back_populates='word') 