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
from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity


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
def search_all_cards():
    try:
        # all_pokemon_set = open('./pokemonSets/all_pokemon.json')
        # all_pokemon = json.load(all_pokemon_set)
        args = request.args
        
        name = args.get('name')

    
        args2= args.to_dict(flat=False)
    
        datalist=[]
        cards=Card.where(q=f'name:{name}*')


        for data in cards:
            datalist.append(data)
    
        return jsonify({
                'success': True,
                'pokemon': datalist
            })

        # if "set[value]" not in args2 and len(args['name']) == 0:
        #     all_pokemon_list=[]
        #     for key,value in all_pokemon.items():
        #         all_pokemon_list.append(value)
            
        #     return jsonify({
        #         'success': True,
        #         'pokemon': all_pokemon_list
        #     })

        # if "set[value]" not in args2 and len(args['name']) > 0:

        #     name = name.title()
        #     name_pokemon = {}
        #     for key, value in all_pokemon.items():
        #         if key == name:
        #             name_pokemon[key] = value
        #         if key.startswith(name):
        #             name_pokemon[key] = value
        #     all_pokemon_list=[]
        #     for key,value in name_pokemon.items():
        #         all_pokemon_list.append(value)
        #     return jsonify({
        #         'success': True,
        #         'pokemon': all_pokemon_list
        #     })
        
        # sets={}
        
        # for x in args2["set[value]"]:
        #     sets[x] = x
    
        
        

        # pokemon_to_return={}
        # if len (sets) != 0:
           
        #     for key, value in all_pokemon.items():
        #         if value['set']['name'] in sets:
        #             pokemon_to_return[key] = value
            
        #     if len((args["name"]))==0:
        #         all_pokemon_list=[]
        #         for key,value in pokemon_to_return.items():
        #             all_pokemon_list.append(value)
        #         return jsonify({
        #             'success': True,
        #             'pokemon': all_pokemon_list
        #         })
        #     else:
        #         filterd={}
        #         for key, value in pokemon_to_return.items():
        #             ne_name=args["name"]
        #             if key == ne_name.title():
        #                 filterd[key] = value
        #             if key.startswith(ne_name.title()):
        #                 filterd[key] = value
        #         all_pokemon_list=[]
        #         for key,value in filterd.items():
        #             all_pokemon_list.append(value)
        #         return jsonify({
        #                 "success": True,
        #                 "pokemon": all_pokemon_list
        #             })       
    except Exception as e:
        print(e)
        abort(422)



@binder.route('/set', methods=['GET'])
def retrieve_all_sets():
    try:
        # all_pokemon_set = open('./pokemonSets/all_pokemon.json')
        # all_pokemon = json.load(all_pokemon_set)

        

        # all_sets = Set.all() # a list of set


        # collections_by_series={} # organize set objs by series collections
        # for set in all_sets:
        #     if set.series not in collections_by_series:
        #         collections_by_series[set.series]=[set]
        #     else:
        #         collections_by_series[set.series]+=[set]


        # output=[] 
        # #convert dict to list
        # for set in collections_by_series:
            
        #     output.append(set)


    

        all_sets = Set.all() # a list of set


        collections_by_series={} # organize set objs by series collections
        for set in all_sets:
            datadict={}
            datadict["setName"]= set.name
            datadict["symbolImage"]= set.images.symbol
            datadict["logo"]= set.images.logo
            datadict["series"]= set.series
            datadict["total"]= set.total
            datadict["releaseDate"]= set.releaseDate
            if set.series not in collections_by_series:
                
                collections_by_series[set.series]=[]

        
            collections_by_series[set.series].append(datadict)
            
        return jsonify({
                'success': True,
                'pokemon': collections_by_series
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