from flask import Flask, redirect, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db
from forms import AddPetForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

#db.create_all()

@app.route("/")
def show_pets():
    pets = Pet.query.all()
    return render_template("show-pets.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """
        shows pet add form and handle its submit action
    """
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"added {{name}}")
        return redirect("/")
    else:
        return render_template("pet-add-form.html", form=form)
    
@app.route("/<int:petId>/edit", methods=["GET", "POST"])
def edit_pet(petId):
    """ shows pet edit form and handle its submit action """
    pet = Pet.query.get_or_404(petId)
    form = AddPetForm(obj=pet)
    
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        # pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"added {{name}}")
        return redirect(f"/{pet.id}/edit")
    else:
        return render_template("edit-pet.html", form=form, pet=pet)
