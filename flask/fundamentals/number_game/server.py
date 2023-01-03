from flask import Flask, render_template, request, redirect, session
from leaderboard import Leaderboard
import random

app = Flask(__name__)
app.secret_key = 'number_guesser'

@app.route('/')
def home_page():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    if 'num_guesses' not in session:
        session['num_guesses'] = 0
    return render_template('index.html')

@app.route('/guess_num', methods=["POST"])
def guess_num():
    if request.form['num'] != "":
        if int(request.form['num']) > session['num']:
            session['guess_status'] = 'high'
        elif int(request.form['num']) < session['num']:
            session['guess_status'] = 'low'
        elif int(request.form['num']) == session['num']:
            session['guess_status'] = 'correct'
        session['num_guesses'] += 1
    return redirect('/')

@app.route('/restart', methods=["POST"])
def restart():
    session['num'] = random.randint(1, 100)
    session['guess_status'] = ""
    session['num_guesses'] = 0
    return redirect('/')

@app.route('/leaderboard')
def leaderboard():
    posts = Leaderboard.get_leaderboard()
    return render_template('leaderboard.html', leaderboard=posts)

@app.route('/leaderboard/new_post', methods=['POST'])
def add_leaderboard_post():
    data = {
        "name": request.form['name'],
        "num_guesses": session['num_guesses']
    }

    Leaderboard.save(data)
    return redirect('/leaderboard')


if __name__ == '__main__':
    app.run(debug=True)