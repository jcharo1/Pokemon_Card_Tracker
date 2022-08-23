import os
from flask import Flask, request, abort, jsonify, flash
# from flask_wtf import form
# from forms import UserForm
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import User, Binder
from flask import current_app, Blueprint, render_template
import json
from auth import AuthError, requires_auth
from jose import jwt
user = Blueprint('user', __name__, url_prefix='/user')


db = SQLAlchemy()

all_pokemon_set = open('pokemonSets/all_pokemon.json')
all_pokemon = json.load(all_pokemon_set)
@user.route('/create', methods=['POST'])
# @requires_auth()
def create_user():
    
    try: 
        body = request.get_json()
        name = body.get('name')
        pokemongo_id = body.get('pokemongo_id')
        
        
        noName = name == "" or name == None
        noPokemongo_id = pokemongo_id == "" or pokemongo_id == None
        if ( (noName) or (noPokemongo_id)):
             return bad_request(400)
        else: 
            user = User(name=name,
            pokemongo_id=pokemongo_id)
            

            db.session.add(user)
            db.session.commit()
            user_id=user.id
            db.session.close()
            
        
    except Exception as e:
        print(e)

        abort(422)
    

    return jsonify({
        'success': True,
        'user_id': user_id,
        })


@user.route('', methods=['GET'])
def retrieve_all_users():
    try:
        users = User.query.all()

        user_list = []

        for user in users:
            user_list.append({
                'id': user.id,
                'name': user.name,
                'verified': user.verified,
                'pokemongo_id': user.pokemongo_id
            })
            
        total_users =len(user_list)

        if (total_users == 0):
            
            return not_found(404)
            
    except Exception as e:
        print(e)
        abort(422)
        

    return jsonify({
            'success': True,
            'users': user_list,
            'total users': len(user_list)

            
        })


@user.route('/<int:id>', methods=['GET'])
@requires_auth()
def retrieve_user_by_id(jwt, id):
    try:
    
        user = User.query.get(id)
        
        noUserid = user == '' or user == None

        if noUserid:
            return not_found(404)    


        binder = user.pokemon_cards
    
        pokemon_binder = []
        baseSet=[]
        for card in binder:
            
            pokemon_id = card.__dict__['pokemon_id']
            print(pokemon_id)
            pokemon_binder.append(all_pokemon[pokemon_id])
            print(all_pokemon[pokemon_id]["set"]["name"])
            

    except Exception as e:
        print(e)
        abort(500)
        

    return jsonify({
            'success': True,
            'id': user.id,
            'name': user.name,
            'verified': user.verified,
            'pokemongo_id': user.pokemongo_id,
            'pokemon_cards': pokemon_binder
            # 'Base_Set':
            # 'Jungle_Set':
            # 'Fossil_Set':

        })





@user.route('/<int:id>', methods=['PATCH'])
@requires_auth('patch:user')
def edit_user(jwt, id):
  
    body = request.get_json()
    name = body.get('name')
    pokemongo_id = body.get('pokemongo_id')
        
    try: 
        
        user = User.query.get(id)
        
        noUserid = user == '' or user == None

        if noUserid:
            return not_found(404)    
        
        noName = name == "" or name == None
        noPokemongo_id = pokemongo_id == "" or pokemongo_id == None
        if ( (noName) or (noPokemongo_id)):
             return bad_request(400)

        db.session.query(User).filter(User.id == id).update({
            User.name:name,
            User.pokemongo_id:pokemongo_id
            })
        
        db.session.commit()
        db.session.close()
        # db.session.query(User).filter(User.id == id ).get

        # user = User.query.get(id)

        

        
    except Exception as e :
        print(e)
        abort(422)
    

    return jsonify({
        'success': True,
        'updated username': user.name,
        'updated pokemonGO id': user.pokemongo_id
        })





@user.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400

@user.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404

@user.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422
