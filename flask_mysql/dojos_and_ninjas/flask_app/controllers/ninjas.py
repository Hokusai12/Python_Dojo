from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def create_ninja():
    return render_template("ninja_form.html", dojos=Dojo.get_dojos())

@app.route("/ninjas/add_ninja", methods=['POST'])
def add_ninja():

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojo_id': request.form['dojo']
    }
    Ninja.save(data)

    return redirect("/dojos/" + str(request.form['dojo']))