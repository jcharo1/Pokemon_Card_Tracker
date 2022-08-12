import os
from flask import Flask, request, abort, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
# from forms import UserForm
from models import db, setup_db, User, Binder
from dotenv import load_dotenv

load_dotenv()

def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    CORS(app)
    
    setup_db(app)
    migrate = Migrate(app, db)
    from routes.user import user
    app.config.from_object('config')
    app.register_blueprint(user)
    from routes.binder import binder
    app.register_blueprint(binder)
    
    return app

app = create_app()

@app.route('/')
def pokemonex():
  return render_template('lol.html')
  



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
