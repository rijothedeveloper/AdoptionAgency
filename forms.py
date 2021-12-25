from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField
from wtforms.validators import URL, AnyOf, InputRequired, NumberRange, Optional, Length

class AddPetForm(FlaskForm):
    """ form for adding pets"""
    
    name = StringField(
        "Pet Name",
        validators=[InputRequired()]
    )

    species = SelectField(
        "Species",
        choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    )

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()]
    )

    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30)]
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)]
    )
    