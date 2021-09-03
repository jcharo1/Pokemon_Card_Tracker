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
  
    body = request.get_json()
    pokemon_id = body.get('pokemon_id')
    user_id = body.get('user_id')

    try: 
        binder = Binder(
        pokemon_id = pokemon_id,
        user_id = user_id
        )
        
        noPokemon_id = pokemon_id == "" or pokemon_id == None
        noUser_id = user_id == "" or user_id == None
        if ( (noPokemon_id) or (noUser_id)):
             return bad_request(400)
        db.session.add(binder)
        db.session.commit()
        db.session.close()
        
        
    except Exception as e:
        print(e)
        abort(422)
    

    return jsonify({
        'success': True,
        'pokemon added': pokemon_id,
        'pokemon card added to user id': user_id

    })

@binder.route('/', methods=['DELETE'])
@requires_auth('delete:card')
def delete_pokemon_card(jwt):
    body = request.get_json()


    try: 

        pokemon_id = body.get('pokemon_id')
        user_id =  body.get('user_id')
        

        deleted = db.session.query(Binder).filter(Binder.pokemon_id == pokemon_id and Binder.user_id == user_id).delete()


        db.session.commit()
        db.session.close()
        
        if deleted == 0:
            return bad_request(400)
        
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

@binder.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400