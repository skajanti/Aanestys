from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///votes.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

from functools import wraps
from flask_login import current_user

def login_required(role="ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user:
                return login_manager.unauthorized()
          
            if not current_user.is_authenticated:
                return login_manager.unauthorized()
            
            unauthorized = False

            if role != "ANY":
                unauthorized = True
                
                if current_user.role == role:
                    unauthorized = False

            if unauthorized:
                return login_manager.unauthorized()
            
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper

from application import views

from application.candidate import models
from application.candidate import views

from application.vote import models
from application.vote import views

from application.auth import models
from application.auth import views

from application.election import models
from application.election import views
from application.election import forms

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try: 
    db.create_all()
except:
    pass
