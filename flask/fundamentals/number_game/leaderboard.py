from mysqlconnection import connectToMySQL

class Leaderboard:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.num_guesses = data['num_guesses']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']

    @classmethod
    def get_leaderboard(cls):
        query = "SELECT * FROM leaderboard;"
        results = connectToMySQL('num_game_leaderboard').query_db(query)

        leaderboard = []
        for post in results:
            leaderboard.append(Leaderboard(post))
        return leaderboard

    @classmethod
    def save(cls, data):
        query = "INSERT INTO leaderboard (name, num_guesses, created_at, updated_at) VALUES (%(name)s, %(num_guesses)s, NOW(), NOW());"
        print(query)
        return connectToMySQL('num_game_leaderboard').query_db(query, data)