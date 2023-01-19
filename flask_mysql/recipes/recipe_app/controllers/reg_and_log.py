from flask import render_template, redirect, request, session, flash
from recipe_app import bcrypt
from recipe_app import app
from recipe_app.models.user import User
import re

@app.route("/")
def reg_and_log():
    return render_template("reg_and_log_forms.html")

@app.route("/process-registration", methods=["POST"])
def process_registration():
    #Validate the form
    if not User.validate_registration(request.form):
        return redirect("/")

    data = {
        "first_name": request.form['first-name'],
        "last_name": request.form['last-name'],
        "email": request.form['email'],
        "pw_hash": bcrypt.generate_password_hash(request.form['password'])
    }

    session['user_id'] = User.save(data)
    return redirect("/recipes")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/validate-login", methods=["POST"])
def validate_login():
    if User.emailInDB(request.form['email']):
        if User.verify_password(request.form['email'], request.form['password']):
            session['user_id'] = User.get_user_id(request.form['email'])
            return redirect("/recipes")
    flash("Invalid login")
    return redirect("/")
    

    
