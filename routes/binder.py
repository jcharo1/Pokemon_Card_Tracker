import os
from flask import Flask, request, abort, jsonify, flash
from flask_wtf import form
from forms import BinderForm
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import User, Binder
from flask import current_app, Blueprint, render_template
binder = Blueprint('binder', __name__, url_prefix='/binder')

db = SQLAlchemy()

@binder.route('/add-card', methods=['POST'])
def add_pokemon_card():
  
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