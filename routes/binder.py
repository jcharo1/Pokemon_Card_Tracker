import os
from flask import Flask, request, abort, jsonify, flash
from flask_wtf import form
from forms import BinderForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select, update, delete, and_
from flask_cors import CORS
from models import User, Binder
from flask import current_app, Blueprint, render_template
import json
from auth import AuthError, requires_auth
from jose import jwt
binder = Blueprint('binder', __name__, url_prefix='/binder')

db = SQLAlchemy()

@binder.route('/', methods=['POST'])
@requires_auth('post:add-card')
def add_pokemon_card(jwt):
  
    # print(request.form)
    # print('------------------------------')
    form = BinderForm(request.form)
    

    try: 
        binder = Binder(
        pokemon_id = form.pokemon_id.data,
        user_id = form.user_id.data
        )
        # print(form.name.data)
        db.session.add(binder)
        db.session.commit()
        db.session.close()
        if binder is None:
            abort(404)
        
    except Exception as e:
        print(e)
        abort(422)
    

    return jsonify({
        'success': True,

    })

@binder.route('/', methods=['DELETE'])
@requires_auth('delete:card')
def delete_pokemon_card(jwt):
    body = request.get_json()
    # print(request.form)
    # print('------------------------------')
    try: 

        pokemon_id = body.get('pokemon_id')
        user_id =  body.get('user_id')
        

        deleted = db.session.query(Binder).filter(Binder.pokemon_id == pokemon_id and Binder.user_id == user_id).delete()


        db.session.commit()
        db.session.close()
        
        if deleted == 0:
            return not_found(404)
        
    except Exception as e:
        print(e)
        abort(422)
    

    return jsonify({
        'success': True,
        'deleted': deleted,

    })




@binder.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404
