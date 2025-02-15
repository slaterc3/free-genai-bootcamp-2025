from invoke import task
from flask import current_app
import yaml
import os

@task
def init_db(ctx):
    """Initialize the database."""
    ctx.run("flask db init")
    print("Database initialized.")

@task
def migrate_db(ctx):
    """Run database migrations."""
    ctx.run("flask db migrate")
    ctx.run("flask db upgrade")
    print("Database migrated.")

@task
def seed_data(ctx):
    """Seed the database with initial data."""
    from app import create_app, db
    app = create_app('development')
    
    with app.app_context():
        seed_dir = os.path.join(app.root_path, 'db', 'seed')
        for filename in sorted(os.listdir(seed_dir)):
            if filename.endswith('.yaml'):
                with open(os.path.join(seed_dir, filename)) as f:
                    data = yaml.safe_load(f)
                    for item in data:
                        model = __import__(item['model'], fromlist=[''])
                        for record in item['data']:
                            obj = model(**record)
                            db.session.add(obj)
                    db.session.commit()
    print("Database seeded.")

@task
def seed_initial_data(ctx):
    """Seed initial data into database."""
    from . import create_app, db
    from .models import Word, Group, StudyActivity
    from .db.seed.initial_data import words_data, groups_data, study_activities_data
    
    app = create_app('development')
    
    with app.app_context():
        # Add words
        for word_data in words_data:
            word = Word(**word_data)
            db.session.add(word)
            
        # Add groups
        for group_data in groups_data:
            group = Group(**group_data)
            db.session.add(group)
            
        # Add study activities
        for activity_data in study_activities_data:
            activity = StudyActivity(**activity_data)
            db.session.add(activity)
            
        db.session.commit() 