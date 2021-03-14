import os
import logging.config
import dash
import dash_bootstrap_components as dbc
from flask import Flask, render_template
from flask_login import LoginManager, login_required
from database import db, User
from config import config

from log_config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)

app = dash.Dash(
    "datyy",
    server=False,
    title="Datyy",
    assets_folder="static",
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        "https://use.fontawesome.com/releases/v5.8.1/css/all.css",
    ],
    url_base_pathname="/datyy/",
    meta_tags=[
        {"charset": "utf-8"},
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1, shrink-to-fit=no",
        },
    ],
)
app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True


def create_server():
    """Creates flask server

    Returns:
        obj: Flask server

    """
    flask_server = Flask(__name__)
    flask_server.config["SECRET_KEY"] = os.urandom(12)
    flask_server.config["SQLALCHEMY_DATABASE_URI"] = config["dburi"]
    flask_server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(flask_server)

    with flask_server.app_context():
        db.init_app(flask_server)
        from routes.main import main as main_blueprint
        from routes.auth import auth as auth_blueprint

        app.init_app(app=flask_server)
        flask_server.register_blueprint(auth_blueprint)
        flask_server.register_blueprint(main_blueprint)

    for view_func in flask_server.view_functions:
        if view_func.startswith("/datyy/"):
            flask_server.view_functions[view_func] = login_required(
                flask_server.view_functions[view_func]
            )

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @flask_server.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    return flask_server


server = create_server()
