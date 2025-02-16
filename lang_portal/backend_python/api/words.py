from flask import jsonify, request
from . import api
from ..models.word import Word
from ..schemas.word import word_schema, words_schema

@api.route('/words', methods=['GET'])
def get_words():
    words = Word.query.all()
    return jsonify(words_schema.dump(words))

@api.route('/words/<int:id>', methods=['GET'])
def get_word(id):
    word = Word.query.get_or_404(id)
    return jsonify(word_schema.dump(word)) 