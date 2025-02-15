from .. import db
from ..models.word import Word

class WordService:
    def get_all(self):
        return Word.query.all()
    
    def get_by_id(self, id):
        return Word.query.get_or_404(id)
    
    def get_paginated(self, page=1, per_page=100):
        return Word.query.paginate(page=page, per_page=per_page) 