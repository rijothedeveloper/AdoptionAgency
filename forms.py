from flask_wtf import FlaskForm
from wtforms import StringField, FloatField

class AddPetForm(FlaskForm):
    """ form for adding pets"""
    
    name = StringField("Pet name")
    species = StringField("Species")
    photo_url = StringField("Photo URL")
    age = StringField("Age")
    notes = StringField("Notes")
    