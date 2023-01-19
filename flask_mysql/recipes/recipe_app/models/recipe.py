from recipe_app.config.mysqlconnection import connectToMySQL
from recipe_app.models.user import User
from flask import flash

class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.dish_name = data["dish_name"]
        self.description = data["description"]
        self.under_thirty_min = bool(data["under_thirty_min"])
        self.instructions = data["instructions"]
        self.date_cooked = data["date_cooked"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.author = None

    @classmethod
    def get_recipe(cls, id):
        data = {
            "id": id
        }
        query = "SELECT * FROM recipes WHERE id=%(id)s;"
        result = connectToMySQL("recipe_schema").query_db(query, data)
        recipe = cls(result[0])
        recipe.author = User.get_user(result[0]["users_id"])
        return recipe


    @classmethod
    def get_all_recipes(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL("recipe_schema").query_db(query)
        all_recipes = []

        for row in results:
            recipe_data = {
                "id": row["id"],
                "dish_name": row["dish_name"],
                "description": row["description"],
                "under_thirty_min": row["under_thirty_min"],
                "instructions": row["instructions"],
                "date_cooked": row["date_cooked"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"]
            }

            recipe = cls(recipe_data)
            recipe.author = User.get_user(row["users_id"])
            
            all_recipes.append(recipe)

        return all_recipes


    @classmethod
    def update_recipe(cls, data):
        query = """UPDATE recipes
        SET dish_name=%(dish_name)s, description=%(description)s, under_thirty_min=%(under_thirty_min)s, instructions=%(instructions)s, date_cooked=%(date_cooked)s, updated_at=NOW()
        WHERE id=%(id)s;
        """
        return connectToMySQL("recipe_schema").query_db(query, data)


    @classmethod
    def save_recipe(cls, data):
        query = """INSERT INTO recipes (dish_name, description, under_thirty_min, instructions, date_cooked, created_at, updated_at, users_id)
        VALUES (%(dish_name)s, %(description)s, %(under_thirty_min)s, %(instructions)s, %(date_cooked)s, NOW(), NOW(), %(users_id)s);"""
        return connectToMySQL("recipe_schema").query_db(query, data)

    @classmethod
    def delete_recipe(cls, id):
        data = {
            "id": id
        }
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        connectToMySQL("recipe_schema").query_db(query, data)

    @classmethod
    def validate_recipe(cls, form_data):
        is_valid = True
        if form_data["date_cooked"] == None or form_data["date_cooked"] == "":
            flash("Date Cooked required")
            is_valid=False
        if "under_thirty_min" not in form_data:
            flash("Under 30 min selection required")
            is_valid = False
        if form_data["dish_name"] == "":
            flash("Dish name required")
            is_valid = False
        if form_data["desc"] == "":
            flash("Dish description required")
            is_valid = False
        if form_data["instructions"] == "":
            flash("Dish instructions required")
            is_valid = False

        return is_valid
