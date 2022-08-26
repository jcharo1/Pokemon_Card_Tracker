import os
from flask import Flask, request, abort, jsonify, flash
# from flask_wtf import form
# from forms import BinderForm
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
@requires_auth()
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
        abort(500)
    

    return jsonify({
        'success': True,
        'pokemon_added': pokemon_id,
        'added_to_id': user_id

    })

@binder.route('/', methods=['DELETE'])
@requires_auth()
def delete_pokemon_card(jwt):
    body = request.get_json()
    print(body)

    try: 

        pokemon_id = body.get('pokemon_id')
        user_id =  body.get('user_id')
        

        deleted = db.session.query(Binder).filter(Binder.pokemon_id == pokemon_id and Binder.user_id == user_id).delete()


        db.session.commit()
        db.session.close()
        
        if deleted == 0:
            return jsonify({
                'success':False,
                'deleted':f"Unable to delete {pokemon_id}, you may not have this card in your Binder"
            })
        
    except Exception as e:
        print(e)
        abort(500)
    

    return jsonify({
        'success': True,
        'deleted': pokemon_id,

    })

@binder.route('/', methods=['GET'])
def retrieve_all_sets():
    try:
        all_pokemon_set = open('./pokemonSets/all_pokemon.json')
        all_pokemon = json.load(all_pokemon_set)
        args = request.args
   
        name = args.get('name')
        

        args2= args.to_dict(flat=False)

    
        if "set[value]" not in args2 and len(args['name']) == 0:
            all_pokemon_list=[]
            for key,value in all_pokemon.items():
                all_pokemon_list.append(value)
            
            return jsonify({
                'success': True,
                'pokemon': all_pokemon_list
            })

        if "set[value]" not in args2 and len(args['name']) > 0:

            name = name.title()
            name_pokemon = {}
            for key, value in all_pokemon.items():
                if key == name:
                    name_pokemon[key] = value
                if key.startswith(name):
                    name_pokemon[key] = value
            all_pokemon_list=[]
            for key,value in name_pokemon.items():
                all_pokemon_list.append(value)
            return jsonify({
                'success': True,
                'pokemon': all_pokemon_list
            })
        
        sets={}
        
        for x in args2["set[value]"]:
            sets[x] = x
    
        
        

        pokemon_to_return={}
        if len (sets) != 0:
           
            for key, value in all_pokemon.items():
                if value['set']['name'] in sets:
                    pokemon_to_return[key] = value
            
            if len((args["name"]))==0:
                all_pokemon_list=[]
                for key,value in pokemon_to_return.items():
                    all_pokemon_list.append(value)
                return jsonify({
                    'success': True,
                    'pokemon': all_pokemon_list
                })
            else:
                filterd={}
                for key, value in pokemon_to_return.items():
                    ne_name=args["name"]
                    if key == ne_name.title():
                        filterd[key] = value
                    if key.startswith(ne_name.title()):
                        filterd[key] = value
                all_pokemon_list=[]
                for key,value in filterd.items():
                    all_pokemon_list.append(value)
                return jsonify({
                        "success": True,
                        "pokemon": all_pokemon_list
                    })       
    except Exception as e:
        print(e)
        abort(422)
        


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