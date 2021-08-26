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

class Binder(db.Model):
    __tablename__ = 'Binder'
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)




