import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_default_secret_key'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
    MODEL_PATH = os.environ.get('MODEL_PATH') or 'app/models/model.pkl'