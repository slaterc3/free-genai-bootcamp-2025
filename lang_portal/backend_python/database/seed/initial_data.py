"""Initial seed data for the database."""

from flask import current_app
from backend_python import create_app, db
from backend_python.models.word import Word
from backend_python.models.group import Group
from backend_python.models.study_activity import StudyActivity

# Keep your existing data arrays
words_data = [
    {
        "characters": "你好",
        "pinyin": "nǐ hǎo",
        "english": "hello",
        "parts": ["你", "好"]
    },
    {
        "characters": "谢谢",
        "pinyin": "xiè xiè",
        "english": "thank you",
        "parts": ["谢", "谢"]
    }
]

groups_data = [
    {
        "name": "Basics",
        "words_count": 2
    }
]

study_activities_data = [
    {
        "name": "Flashcards",
        "url": "/study/flashcards"
    },
    {
        "name": "Multiple Choice",
        "url": "/study/multiple-choice"
    }
]

def seed_initial_data():
    """Seed initial data into the database."""
    app = create_app()
    with app.app_context():
        try:
            print("Creating study activities...")
            activities = [StudyActivity(**data) for data in study_activities_data]
            
            print("Creating groups...")
            groups = [Group(**data) for data in groups_data]
            
            print("Creating words...")
            words = []
            for data in words_data:
                parts = data.get('parts', [])
                word = Word(
                    characters=data['characters'],
                    pinyin=data['pinyin'],
                    english=data['english'],
                    parts=parts
                )
                print(f"Created word: {word.characters}")
                words.append(word)
            
            print("Adding to session...")
            for activity in activities:
                db.session.add(activity)
            for group in groups:
                db.session.add(group)
            for word in words:
                db.session.add(word)
            
            print("Committing...")
            db.session.commit()
            print("Commit successful!")
        except Exception as e:
            print(f"Error: {str(e)}")
            db.session.rollback()
            raise e 