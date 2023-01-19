from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def show_dojos():
    dojos = Dojo.get_dojos()
    return render_template("dojos.html", dojos=dojos)

@app.route("/dojos/create-dojo", methods=['POST'])
def create_dojo():
    data = {
        'name': request.form['name']
    }
    Dojo.save_dojo(data)
    return redirect("/dojos")

@app.route("/dojos/<int:id>")
def show_dojo(id):
    data = {
        'id': id
    }
    dojo = Dojo.get_dojo_with_ninjas(data)
    return render_template("select_dojo.html", dojo=dojo)

@app.route("/dojos/edit/<int:id>")
def edit_dojo(id):
    data = {
        "id": id
    }
    return render_template("edit_dojo.html", dojo=Dojo.get_dojo(data))

@app.route("/dojos/update/<int:id>", methods=["POST"])
def update_dojo(id):
    data = {
        "name": request.form['name'],
        "id": id
    }
    Dojo.update_dojo(data)
    return redirect("/dojos")