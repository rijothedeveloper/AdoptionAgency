from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import URL, AnyOf, InputRequired, NumberRange

class AddPetForm(FlaskForm):
    """ form for adding pets"""
    
    name = StringField("Pet name", validators=[InputRequired(message="name is required")])
    validSpecies = ["cat", "dog","porcupine"]
    species = StringField("Species", validators=[AnyOf(values=['cat', 'dog','porcupine'], message="species should be either cat, dog, or porcupine" )])
    photo_url = StringField("Photo URL", validators=[URL(require_tld=True, message="need a vlid url")])
    # age = StringField("Age", validators=[NumberRange(min=0, max=10, message='bla')])
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = StringField("Age")
    notes = StringField("Notes")
    