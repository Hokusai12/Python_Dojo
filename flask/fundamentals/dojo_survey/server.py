from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = 'this is the secret key for the codingdojo dojo survey assignment'

@app.route('/')
def survey_page():
    return render_template('form_page.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['name'] = request.form['name']
    session['dojo_loc'] = request.form['dojo_loc']
    session['fav_lang'] = request.form['fav_lang']
    session['comment'] = request.form['comment']
    session['enrollment'] = request.form['enrollment']
    session['stacks'] = request.form.getlist('stacks')
    return redirect('/result')

@app.route('/result')
def display_results():
    return render_template('result_page.html', name=session['name'], enrollment=session['enrollment'], stacks=session['stacks'], dojo_loc=session['dojo_loc'], fav_lang=session['fav_lang'], comment=session['comment'])

if __name__ == '__main__':
    app.run(debug=True)