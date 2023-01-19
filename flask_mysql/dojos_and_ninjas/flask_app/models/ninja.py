from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, created_at, updated_at, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s);"
        print(query)
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_ninja(cls, data):
        query = "SELECT * FROM ninjas WHERE id=%(id)s;"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        ninja = cls(result[0])
        return ninja

    @classmethod
    def update_ninja(cls, data):
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)