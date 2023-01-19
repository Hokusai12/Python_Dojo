from recipe_app import app, bcrypt
from recipe_app.controllers import reg_and_log, recipes


if __name__=="__main__":
    app.run(debug=True)