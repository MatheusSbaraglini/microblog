"""configs"""
# Define the application directory
import os
import sys


DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# Define the database - SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

# Secret key
SECRET_KEY = "secret"
