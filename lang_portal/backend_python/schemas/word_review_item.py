from .. import ma
from ..models.word_review_item import WordReviewItem

class WordReviewItemSchema(ma.SQLAlchemySchema):
    class Meta:
        model = WordReviewItem
        
    id = ma.auto_field()
    word_id = ma.auto_field()
    study_session_id = ma.auto_field()
    correct = ma.auto_field()
    created_at = ma.auto_field()
    
    # Nested relationships
    word = ma.Nested('WordSchema', exclude=('review_items',)) 