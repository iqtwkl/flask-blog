import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'some-key'
    SQLALCHEMY_DATABASE_URI = "postgresql://"+os.environ.get('DATABASE_USER')+":"+os.environ.get('DATABASE_PASS')+"@"+os.environ.get('DATABASE_URL')+"/flask_blog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False