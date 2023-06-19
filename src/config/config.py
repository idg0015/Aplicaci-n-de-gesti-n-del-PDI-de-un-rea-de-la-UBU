import os


class Config(object):
    SECRET_KEY = os.urandom(12)
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINISTRATOR_EMAIL = 'idg0015@alu.ubu.es'
    # La configuración de las sesiones está en el archivo app.py. Necersario por el orden de carga de los módulos
