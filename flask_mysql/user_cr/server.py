from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)

@app.route('/users')
def display_users():
    return render_template("users.html", all_users=User.get_all())

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

    User.save(data)
    return redirect('/users')

@app.route('/')
def reroute():
    return render_template('reroute.html')

if __name__ == '__main__':
    app.run(debug=True)