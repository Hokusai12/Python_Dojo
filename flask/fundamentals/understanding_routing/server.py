from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/dojo")
def say_dojo():
    return "Dojo!"

@app.route("/say/<string:word>")
def say_hi(word):
    return f"Hi {word}!"

@app.route("/repeat/<int:num>/<string:word>")
def repeat(num, word):
    return f"{word * num}"

@app.route("/<path:path>")
def catch_all(path):
    return "Sorry! No response. Try again!"

if __name__ == '__main__':
    app.run(debug=True)
