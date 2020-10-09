from flask import Flask
import os
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from os import environ, path
import pymysql
from dotenv import load_dotenv




app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))



app.config['SECRET_KEY']='mrvyuvbkiuybkiuniuyiuy'  #environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI']=environ.get('CLEARDB_PINK_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['DROPBOX_TOKEN'] = environ.get('DROPBOX_TOKEN')
#app.config['FLASK_APP'] = #environ.get('FLASK_APP')
#app.config['DEBUG'] = #environ.get('DEBUG')
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    "pool_size":20,
    "pool_pre_ping":True,
    "pool_recycle": 3600,
}





############################
### DATABASE SETUP ##########
#############################
db = SQLAlchemy(app)
Migrate(app,db)

#####################
####connecting the routes to our app####S
########################

from temibot.users.views import users
app.register_blueprint(users)
