import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'secret!'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'messages.db')

class ProductionConfig(Config):

    #DATABASE_URI = 'mysql://user@localhost/foo'
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    #SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:3306/%s' %(DB_USERNAME,DB_PASSWORD,MARIA_D,BLOG_DATABASE_NAME)
    #DATABASE_NAME = 'MessagesApp'
    #MARIA_D = '172.17.0.1'
    #DB_USERNAME = 'pkyeiuuliulvll'
    DB_PASSWORD = '3V9brJhnXLABJPmP1nLEVp0kXL'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
