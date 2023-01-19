from flask import render_template, redirect, request, session, flash
from dojo_wall_app import bcrypt
from dojo_wall_app import app
from dojo_wall_app.models.user import User

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
    return redirect("/wall_page")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/validate-login", methods=["POST"])
def validate_login():
    if User.emailInDB(request.form['email']):
        if User.verify_password(request.form['email'], request.form['password']):
            session['user_id'] = User.get_user_id(request.form['email'])
            return redirect("/wall_page")  #Change this once you get the posts setup
    flash("Invalid login")
    return redirect("/")