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

@app.route("/ninjas/edit/<int:id>")
def edit_ninja(id):
    data = {
        "id": id
    }
    return render_template("edit_ninja.html", ninja=Ninja.get_ninja(data))

@app.route("/ninjas/update", methods=["POST"])
def update_ninja():
    data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    Ninja.update_ninja(data)
    return redirect("/dojos/" + request.form["dojo_id"])

@app.route("/ninjas/delete/<int:dojo_id>/<int:ninja_id>")
def delete_ninja(dojo_id, ninja_id):
    data = {
        'id': ninja_id
    }
    Ninja.delete_ninja(data)
    return redirect("/dojos/" + str(dojo_id))