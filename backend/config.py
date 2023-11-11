import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_string_for_development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://robinsonjason761@gmail.com:h@Tm7K!Mc9@localhost:5432/drugsafetydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

import os

class DevelopmentConfig:
    # Enables debug mode to provide detailed error logs and auto-reload
    DEBUG = True
    
    # The database URI that should be used for the connection
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://robinsonjason761@gmail.com:h@Tm7K!Mc9@localhost:5432/drugsafetydb'
    
    # Track modifications of objects and emit signals. This requires extra memory and should be disabled if not needed.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Secret key for session management and CSRF protection, use a random value for production
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_string_for_development'
    
    # You can add more configuration options as needed
    # ...

# You may also define other config classes for production, testing, etc.
class ProductionConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/prod_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_production_secret_key'
    # Other production-specific settings

# You can add more configuration classes if you have multiple environments

