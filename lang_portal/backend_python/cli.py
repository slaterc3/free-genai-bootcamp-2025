import click
from flask.cli import with_appcontext
from . import db, create_app  # Back to relative import

@click.command('seed-initial-data')
@with_appcontext
def seed_initial_data_command():
    """Seed initial data into the database."""
    try:
        print("Starting seed process...")
        app = create_app()
        with app.app_context():
            from .database.seed.initial_data import seed_initial_data  # Updated path
            seed_initial_data()
        print("Seed process completed!")
        click.echo('Database seeded with initial data.')
    except Exception as e:
        print(f"Error in seed process: {str(e)}")
        raise e 