from flask import jsonify, request
from . import api
from ..services.word_service import WordService
from ..schemas.word import WordSchema

word_service = WordService()
word_schema = WordSchema()
words_schema = WordSchema(many=True)

@api.route('/words', methods=['GET'])
def get_words():
    """Get paginated list of words"""
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 100, type=int)
    words = word_service.get_paginated(page, per_page)
    return jsonify(words_schema.dump(words.items))

@api.route('/words/<int:id>', methods=['GET'])
def get_word(id):
    """Get a specific word's details"""
    word = word_service.get_by_id(id)
    return jsonify(word_schema.dump(word)) 