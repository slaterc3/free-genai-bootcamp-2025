"""Test file to verify all required packages are properly installed."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from invoke import task

app = Flask(__name__)
db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()

print("All imports successful!") 