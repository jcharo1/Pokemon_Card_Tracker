import os
from flask import Flask, request, abort, jsonify, flash
from flask_wtf import form
from forms import UserForm
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import User, Binder
from flask import current_app, Blueprint, render_template
import json
user = Blueprint('user', __name__, url_prefix='/user')


db = SQLAlchemy()

all_pokemon_set = open('pokemonSets/all_pokemon.json')
all_pokemon = json.load(all_pokemon_set)
@user.route('/create', methods=['POST'])
def create_user():
  
    # print(request.form)
    # print('------------------------------')
    form = UserForm(request.form)
    

    try: 
        user = User(
        name = form.name.data,
        pokemongo_id = form.pokemongo_id.data
        #   verified = form.verified.data
        )
        # print(form.name.data)
        db.session.add(user)
        db.session.commit()
        db.session.close()
        if user is None:
            abort(404)
        
    except:
        abort(422)
    

    return jsonify({
        'success': True,

    })

@user.route('/', methods=['GET'])
def retrieve_all_users():
    try:
        users = User.query.all()
        # print(users)
        # user = User.query.order_by('id').all()
        user_list = []

        for user in users:
            user_list.append({
                'id': user.id,
                'name': user.name,
                'verified': user.verified,
                'pokemongo_id': user.pokemongo_id
            })
        # print(user_list)
        

        if users is None:
            abort(404)
            
    except Exception as e:
        print(e)
        abort(422)
        

    return jsonify({
            'success': True,
            'users': user_list

        })


@user.route('/<int:id>', methods=['GET'])
def retrieve_user_by_id(id):
    try:
        user = User.query.get(id)
        # users = User.query.all()

        binder = user.pokemon_cards
        # print(binder)
        pokemon_binder = []

        for card in binder:
            pokemon_id = card.__dict__['pokemon_id']
            pokemon_binder.append(all_pokemon[pokemon_id])

            
            # print(all_pokemon[pokemon_id])
            # print(card.__dict__['pokemon_id'])



        if user is None:
            abort(404)



    except Exception as e:
        print(e)
        abort(422)
        

    return jsonify({
            'success': True,
            'id': user.id,
            'name': user.name,
            'verified': user.verified,
            'pokemongo_id': user.pokemongo_id,
            'pokemon_cards': pokemon_binder

        })


  






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
