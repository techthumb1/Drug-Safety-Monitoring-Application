import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard_to_guess_string_for_development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://robinsonjason761@gmail.com:h@Tm7K!Mc9@localhost:5432/drugsafetydb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
