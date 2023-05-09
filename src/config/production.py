import os
from config.config import Config


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('JAWSDB_MARIA_URL')

