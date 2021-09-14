from flask import Blueprint, render_template, redirect, url_for, request, flash
from . import db
from .models import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        # If user exists with that email
        if user:
            # If a password is the same which
            # password in our database with that email
            if check_password_hash(user.password, password):
                flash("Logged In!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Password is incorrect!", category="error")
        # If user doesn't exists
        else:
            flash("Email dosn't exists!", category="error")
    return render_template("login.html", user=current_user)


@auth.route("/sign-up", methods=["GET", "POST"])
def signUp():
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        emailExists = User.query.filter_by(email=email).first()
        usernameExists = User.query.filter_by(username=username).first()

        if emailExists:
            flash("Email is already in use!", category="error")
        elif usernameExists:
            flash("Username is already in use!", category="error")
        elif password1 != password2:
            flash("Password don't match!", category="error")
        elif len(username) < 2:
            flash("Username is too short!", category="error")
        elif len(password1) < 6:
            flash("Password is too short!", category="error")
        elif len(email) < 4:
            flash("Email is invalid!", category="error")
        else:
            newUser = User(email=email, username=username,
                           password=generate_password_hash(password1,
                                                           method="sha256"))
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser, remember=True)
            flash("User created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("views.home"))
