## Creates the application object as an instance of class 'Flask'

## (1) Import 'Flask' class from 'flask' Module (and others, 4, 5)
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

## (2) instantiate application object
## Python predefined variable: __name__ for the name of the
##   module in which it is used
app = Flask(__name__)

## (4) Tell Flask to read the config file.
app.config.from_object(Config)

## (5) Create 'db' object that represents the database.
##     Create 'migrate' object that represents the migration engine.
db = SQLAlchemy(app)
migrate = Migrate(app, db)

## (3) Import other modules at the bottom to prevent
##     'circular imports' in loaded modules.
from app import routes, models
