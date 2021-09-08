https://git.heroku.com/pokemon-card-tracker.git
postgres://hghoipaihwgztm:0ab941d2c324b024b5c853c513109a6caa9a906203382a75476352c1561a5cf6@ec2-44-196-8-220.compute-1.amazonaws.com:5432/dp13187l4jlff
https://fsnd778.us.auth0.com/authorize?audience=pokemon&response_type=token&client_id=0nNpheAYkXJwpOiKUOFlBRRAkU2Jk8U7&redirect_uri=https://127.0.0.1:8080/login-results




import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
db = SQLAlchemy()

database_path = os.getenv('DATABASE_URL')


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):

    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    pokemongo_id = db.Column(db.String(), nullable=False)
    pokemon_cards = db.relationship('Binder', backref='user', lazy=True)

class Binder(db.Model):
    __tablename__ = 'Binder'
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)