from flask import Flask, render_template, jsonify, request
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
    print(request.form)
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }

    user = User.get_user(User.save(data))
    user_data = {
        "id": user.id,
        "firstName": user.first_name,
        "lastName": user.last_name,
        "email": user.email
    }

    return jsonify(user_data)

@app.route('/')
def reroute():
    return render_template('reroute.html')

if __name__ == '__main__':
    app.run(debug=True)