from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play")
def three_boxes():
    return render_template("index.html", num_boxes = 3)

@app.route("/play/<int:num>")
def set_boxes(num):
    return render_template("index.html", num_boxes = num)

@app.route("/play/<int:num>/<string:color>")
def set_colored_boxes(num, color):
    return render_template("index.html", num_boxes = num, box_color = color)

if __name__ == '__main__':
    app.run(debug=True)