from asyncio.log import logger
from pathlib import Path
import os
from dotenv import load_dotenv

basedir=os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    FLASK_ENV = 'development'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_URL_DB')
        
class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_RECORD_QUERIES = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PROD_URL_DB')
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app):
    configuration = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    return configuration[app]

USER_DB=os.environ.get('USER_DB')
PASS_DB=os.environ.get('PASS_DB')
URL_DB=os.environ.get('URL_DB')
NAME_DB=os.environ.get('NAME_DB')

DEV_URL_DB=f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:5432/{NAME_DB}"
PROD_URL_DB=f"postgresql://{USER_DB}:{PASS_DB}@{URL_DB}:5432/{NAME_DB}"
print(DEV_URL_DB)
print(PROD_URL_DB)
