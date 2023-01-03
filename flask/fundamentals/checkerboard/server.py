from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def standard():
    return render_template('index.html', x=8, y=8)

@app.route('/<int:y>')
def four_high(y):
    return render_template('index.html', x=8, y=y, color1="red", color2="black")


@app.route('/<int:x>/<int:y>')
def variable_dimension(x, y):
    return render_template('index.html', x=x, y=y, color1="red", color2="black")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard_setup(x, y, color1, color2):
    return render_template('index.html', x=x, y=y, color1=color1, color2=color2)


if __name__ == '__main__':
    app.run(debug =True)