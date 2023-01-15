from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.user import User

@app.route('/users')
def display_users():
    return render_template("users.html", all_users=User.get_all())

@app.route('/users/<int:user_id>')
def display_user(user_id):
    return render_template("specific_user.html", user=User.get_one_user(user_id))

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    return render_template("edit_user.html", user=User.get_one_user(user_id))

@app.route('/update_user', methods=['POST'])
def save_edit():
    data = {
        'id': request.form['user_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.update(data)
    return redirect('/users/' + str(request.form['user_id']))

@app.route('/users/new')
def new_user_form():
    return render_template('create_user.html')

@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }

    user_id = User.save(data)
    return redirect('/users/' + str(user_id))

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    User.delete_user(user_id)
    return redirect('/users')

@app.route('/')
def reroute():
    return render_template('reroute.html')