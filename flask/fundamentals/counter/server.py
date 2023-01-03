from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'blah lahblahblahblaaka'

@app.route('/')
def homepage():
    if 'counter' in session and 'inc_counter' in session: 
        print("Counter has been initialized")
        session['inc_counter'] += 1
        session['counter'] += 1
    else:
        print("Counter hasn't been initialized")
        session['inc_counter'] = 0
        session['counter'] = 0
    return render_template('index.html')

@app.route('/plus_two')
def increment_two():
    if 'counter' in session:
        print('Counter has been initialized')
        session['inc_counter'] += 1
    else:
        print('Counter isn\'t initialized yet')
        session['inc_counter'] = 1
    return redirect('/')

@app.route('/destroy_session')
def reset_counter():
    session.clear()
    return redirect('/')

@app.route('/spec-increment', methods=['POST'])
def spec_increment():
    session['inc_counter'] += int(request.form.get('increment')) - 1
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)