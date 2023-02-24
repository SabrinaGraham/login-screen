import os 
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    DEBUG = False
    SECRET_KEY = os.environ.get ('SECRET_KEY', 'Som3$ecr3tk*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','postgresql://sabby:thel0gger@localhost/logindata'.replace('postgres://','postgres://'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False