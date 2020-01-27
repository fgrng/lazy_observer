import os
basedir = os.path.abspath(os.path.dirname(__file__))

## Configuration settings are defined as class variables
##   inside the 'Config' class.
class Config(object):

    ## Create a secret key -- often used as a cryptographic key for eg CSRF.
    ##   Use environment variable. Use hardcoded string, if env not present.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    ## Use a SQLite database.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'lazy_observer.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
