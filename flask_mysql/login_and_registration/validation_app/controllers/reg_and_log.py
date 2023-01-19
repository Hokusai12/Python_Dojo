from flask import render_template, redirect, request, session, flash
from validation_app import bcrypt
from validation_app import app
from validation_app.models.user import User
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
    return redirect("/welcome_user")

@app.route("/welcome_user")
def welcome_page():
    if "user_id" not in session:
        return redirect("/")
    return render_template("home_page.html", user=User.get_user(session['user_id']))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/validate-login", methods=["POST"])
def validate_login():
    if User.emailInDB(request.form['email']):
        if User.verify_password(request.form['email'], request.form['password']):
            session['user_id'] = User.get_user_id(request.form['email'])
            return redirect("/welcome_user")
    flash("Invalid login")
    return redirect("/")
    

    
