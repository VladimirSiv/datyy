from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    """GET / function

    Returns:
        obj: Render template object

    """
    return render_template("index.html")
