import os


class Config:
    # ... other configurations
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://your_user:your_password@localhost:5432/your_database_name'
