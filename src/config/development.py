from config.config import Config


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/ubu'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
