from flask import render_template, redirect, session, request
from recipe_app.models.user import User
from recipe_app.models.recipe import Recipe
from recipe_app import app

@app.route("/recipes")
def show_welcome_page():
    if "user_id" not in session:
        return redirect("/")
    return render_template("home_page.html", user=User.get_user(session['user_id']), recipes=Recipe.get_all_recipes())

@app.route("/recipes/<int:id>")
def display_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    return render_template("view_recipe.html", user=User.get_user(session["user_id"]), recipe=Recipe.get_recipe(id))

@app.route("/recipes/edit/<int:id>")
def edit_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    return render_template("edit_recipe.html", user=User.get_user(session["user_id"]), recipe=Recipe.get_recipe(id))

@app.route("/recipes/new")
def create_recipe():
    if "user_id" not in session:
        return redirect("/")
    return render_template("add_recipe.html", user=User.get_user(session["user_id"]))

@app.route("/recipes/update_recipe", methods=["POST"])
def update_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect("/recipes/edit/" + str(request.form["recipe_id"]))
    recipe_data = {
        "id": request.form["recipe_id"],
        "dish_name": request.form["dish_name"],
        "description": request.form["desc"],
        "instructions": request.form["instructions"],
        "date_cooked": request.form["date_cooked"],
        "under_thirty_min": request.form["under_thirty_min"]
    }
    Recipe.update_recipe(recipe_data)
    return redirect("/recipes/" + str(request.form["recipe_id"]))

@app.route("/recipes/add_recipe", methods=["POST"])
def add_recipe():
    if not Recipe.validate_recipe(request.form):
        return redirect("/recipes/new")
    recipe_data = {
        "dish_name": request.form["dish_name"],
        "description": request.form["desc"],
        "instructions": request.form["instructions"],
        "date_cooked": request.form["date_cooked"],
        "under_thirty_min": request.form["under_thirty_min"],
        "users_id": session["user_id"]
    }
    recipe_id = Recipe.save_recipe(recipe_data)
    return redirect("/recipes/" + str(recipe_id))

@app.route("/recipes/delete/<int:id>")
def delete_recipe(id):
    if "user_id" not in session:
        return redirect("/")
    Recipe.delete_recipe(id)
    return redirect("/recipes")