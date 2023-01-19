from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "coding_dojo_wall_secret_key"
bcrypt = Bcrypt(app)