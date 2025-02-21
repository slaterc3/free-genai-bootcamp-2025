from .. import ma
from ..models.word import Word

class WordSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Word
        
    id = ma.auto_field()
    characters = ma.auto_field()
    pinyin = ma.auto_field()
    english = ma.auto_field()
    parts = ma.auto_field()
    created_at = ma.auto_field() 

# Create schema instances
word_schema = WordSchema()
words_schema = WordSchema(many=True) 