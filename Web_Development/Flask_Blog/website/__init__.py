from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME = "database.db"


def createApp():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "helloworld"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_perfix="/")
    app.register_blueprint(auth, url_perfix="/")

    from .models import User, Post, Comment, Like

    createDatabase(app)

    loginManager = LoginManager()
    loginManager.login_view = "auth.login"
    loginManager.init_app(app)

    @loginManager.user_loader
    def loadUser(id):
        return User.query.get(int(id))

    return app


def createDatabase(app):
    if not os.path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created database!")
