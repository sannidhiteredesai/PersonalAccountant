import os
from dotenv import load_dotenv

# Load .env file
load_dotenv('.env')


# Define Config object once the .env is loaded
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DB = os.environ.get('DB') or 'db.json'
    # Set logger if required
