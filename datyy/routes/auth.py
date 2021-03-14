from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from database import User
from server import app

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    """GET login function

    Returns:
        obj: Render template

    """
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    """POST login function

    Returns:
        obj: Redirect url object

    """
    username = request.form.get("username")
    password = request.form.get("password")
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password, password):
        app.logger.warning("User failed to log in: %s", username)
        flash("Please check your login details and try again")
        return redirect(url_for("auth.login"))
    login_user(user)
    app.logger.info("User successfully logged in: %s", username)
    return redirect("/datyy/")


@auth.route("/logout")
def logout():
    """GET logout function

    Returns:
        obj: Redirect url object

    """
    logout_user()
    return redirect(url_for("main.index"))
