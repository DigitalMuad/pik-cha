"""
Database initialization script for Render deployment
"""
import os
import sys

# Add server directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from config import create_app, db
from models.user import User
from models.image import Image


def init_database():
    """Initialize the database with all tables"""
    # Create app instance
    app = create_app("production")
    
    with app.app_context():
        # Create instance directory if it doesn't exist
        instance_dir = os.path.join(os.getcwd(), '..', 'instance')
        os.makedirs(instance_dir, exist_ok=True)
        
        # Create all tables
        db.create_all()
        print("✓ Database tables created successfully")
        
        # Check if any users exist
        user_count = User.query.count()
        print(f"✓ Found {user_count} users in database")


if __name__ == '__main__':
    init_database()
