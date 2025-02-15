from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from .config import config
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Create the extensions
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    # Register CLI commands
    from .cli import seed_initial_data_command
    app.cli.add_command(seed_initial_data_command)

    return app 