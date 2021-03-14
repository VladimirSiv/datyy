#!/usr/bin/env python

from flask_login import UserMixin
from sqlalchemy import Table, create_engine
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from config import config

engine = create_engine(config["dburi"])
db = SQLAlchemy()


class User(UserMixin, db.Model):
    """User class

    Atrributes:
        id (int): User id
        username (str): User username
        email (str): User email
        password (str): User password

    """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))


user_table = Table("users", User.metadata)


def create_user_table():
    """Creates user table"""
    User.metadata.create_all(engine)


def add_user(username, password, email):
    """Adds user to the database

    Arguments:
        username (str): User username
        password (str): User password
        email (str): User email

    """
    hashed_pwd = generate_password_hash(password, method="sha256")
    ins = user_table.insert().values(username=username, email=email, password=hashed_pwd)
    conn = engine.connect()
    conn.execute(ins)
    conn.close()


if __name__ == "__main__":
    create_user_table()
    add_user("test", "test", "test")
