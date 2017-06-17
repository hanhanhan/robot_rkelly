import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    ADMIN = os.environ.get('ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS=True

    # # postgresql://username:password@hostname/database
    DATABASE_USER = os.environ.get('DATABASE_USER')
    DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
    HOSTNAME = os.environ.get('HOSTNAME')
    DATABASE = os.environ.get('DATABASE')

    # SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOSTNAME}/{DATABASE}'
    SQLALCHEMY_DATABASE_URI ='postgresql://rkelly:hello@localhost/rkelly'
    # SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOSTNAME}/{DATABASE}'


    @staticmethod
    def init_app(app):
        # db.create_all
        pass
        
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    
    # postgresql://username:password@hostname/database
    # DATABASE_USER = os.environ.get('DATABASE_USER')
    #PASSWORD = os.environ.get('DATABASE_PASSWORD')
    # HOSTNAME = os.environ.get('HOSTNAME')
    # DATABASE = os.environ.get('DATABASE')

    # Or just hardcode once as one thing in .env file? or something else?

    # SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{HOSTNAME}/{DATABASE}'
    pass

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig # 'default': os.environ.get('FLASK_CONFIG')
    }



