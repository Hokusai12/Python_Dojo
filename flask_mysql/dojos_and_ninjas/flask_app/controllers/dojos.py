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