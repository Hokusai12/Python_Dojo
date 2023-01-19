from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []
        
        for dojo in results:
            dojos.append(cls(dojo))
        
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id=ninjas.dojo_id WHERE dojos.id=%(id)s;"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        dojo = cls(result[0])

        for row in result:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at'],
                'dojo_id': dojo.id
            }
            dojo.ninjas.append( Ninja(ninja_data) ) 

        return dojo

    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        print(query)
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    @classmethod
    def get_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id=%(id)s;"
        result = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)
        dojo = cls(result[0])
        return dojo

    @classmethod   
    def update_dojo(cls, data):
        query = "UPDATE dojos SET name=%(name)s WHERE id=%(id)s;"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)