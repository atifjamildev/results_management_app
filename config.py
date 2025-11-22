import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    SECRET_KEY = os.environ.get('SECRET_KEY', None) or 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'school.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
