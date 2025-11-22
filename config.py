import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    SECRET_KEY = os.getenv('SECRET_KEY') or 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'database/school.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
