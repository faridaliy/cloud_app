import os
import sys

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from app.models import User

with app.app_context():
    db.create_all()
    print("Database and tables created successfully!")