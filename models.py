from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    verified = db.Column(db.Boolean, default=False)
    pokemongo_id = db.Column(db.String(), nullable=False)

class Cards_table(db.Model):
    __tablename__ = 'cards_table'
    id = db.Column(db.Integer, primary_key=True)
    pokemon_id = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)
  