from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, BooleanField


class UserForm(Form):
    name = StringField(
        'name'
    )
    pokemongo_id = StringField(
        'pokemongo_id' 
    )
    verified = BooleanField( 'verified' 
    )



class BinderForm(Form):
    pokemon_id = StringField(
        'pokemon_id'
    )
    user_id = StringField(
        'user_id' 
    )