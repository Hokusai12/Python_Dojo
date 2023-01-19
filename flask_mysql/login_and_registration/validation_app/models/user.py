from flask import flash
from validation_app import bcrypt
from validation_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw_hash = data['pw_hash']

    @classmethod
    def get_user_id(cls, email):
        query = "SELECT id FROM users WHERE email=%(email)s;"
        data = {
            "email": email
        }
        result = connectToMySQL("registration_schema").query_db(query, data)
        return result[0]['id']

    @classmethod
    def get_user(cls, id):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        data = {
            "id": id
        }
        print("Got here!")
        result = connectToMySQL("registration_schema").query_db(query, data)
        print(result)
        user = cls(result[0])
        return user

    @classmethod
    def verify_password(cls, email, pswd):
        query = "SELECT * FROM users WHERE email=%(email)s;"
        data = {
            'email': email
        }
        result = connectToMySQL("registration_schema").query_db(query, data)
        user = cls(result[0])
        return bcrypt.check_password_hash(user.pw_hash, pswd)

    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) 
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, NOW(), NOW());"""
        return connectToMySQL("registration_schema").query_db(query, data)

    @staticmethod
    def emailInDB(email):
        query = "SELECT id FROM users WHERE email=%(email)s"
        data = {
            'email': email
        }
        result = connectToMySQL("registration_schema").query_db(query, data)
        if len(result) < 1:
            return False
        return True

    @staticmethod
    def validate_registration(form_data):
        is_valid = True

        if not form_data['first-name'].isalpha() or not form_data['last-name'].isalpha():
            flash("Please only use alphabetic characters in your name")
            is_valid = False
        if len(form_data['first-name']) < 2 or len(form_data['last-name']) < 2:
            flash("Name must be at least 2 characters")
            is_valid = False
        if not EMAIL_REGEX.match(form_data['email']):
            flash("Invalid email")
            is_valid = False
        if User.emailInDB(form_data['email']):
            flash("There is already an account with that email")
            is_valid = False
        if len(form_data['password']) < 8:
            flash("Password must be at least 8 characters")
            is_valid = False
        if not bool(re.search('\d', form_data['password'])):
            flash("Password needs a number")
            is_valid = False
        if not bool(re.search('[A-Z]', form_data['password'])):
            flash("Password needs a capital letter")
            is_valid = False
        if form_data['confirm-password'] != form_data['password']:
            flash("Make sure the passwords match")
            is_valid = False
        return is_valid