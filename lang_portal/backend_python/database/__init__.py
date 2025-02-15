"""Database initialization and utilities."""

def seed_db():
    """Seed the database with initial data."""
    from .seed.initial_data import seed_initial_data
    seed_initial_data() 