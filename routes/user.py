import os
from flask import Flask, request, abort, jsonify, flash
from flask_wtf import form
from forms import UserForm
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import User
from flask import current_app, Blueprint, render_template
user = Blueprint('user', __name__, url_prefix='/user')

db = SQLAlchemy()

@user.route('/create', methods=['POST'])
def create_user():
  
    # print(request.form)
    # print('------------------------------')
    form = UserForm(request.form)
    

    # try: 
    user = User(
    name = form.name.data,
    pokemongo_id = form.pokemongo_id.data
    #   verified = form.verified.data
    )
    print(form.name.data)
    db.session.add(user)
    db.session.commit()
    flash('User ' + request.form['name'] + ' was successfully added!')
    # except ValueError as e:
    #     print(e)
    #     flash('An error occurred. Venue ' + form.name.data + ' could not be listed.')
    # finally:
    #     db.session.close()
    #     print('=============wemadeit-----------------------------')
    return {}

  
