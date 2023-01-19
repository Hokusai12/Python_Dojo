from dojo_wall_app.config.mysqlconnection import connectToMySQL
from dojo_wall_app.models.user import User
from dojo_wall_app.models.comment import Comment

class Post:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.creator = None
        self.comments = []

    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM posts JOIN users ON posts.users_id = users.id;"
        results = connectToMySQL("coding_dojo_wall").query_db(query)
        all_posts = []
        for row in results:
            post = cls(row)
            author_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "pw_hash": row["pw_hash"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            author = User(author_data)
            post.creator = author
            post.comments = Comment.get_comments_for_post(post)
            all_posts.append(post)
        return all_posts

    @classmethod 
    def save_post(cls, data):
        query = "INSERT INTO posts (content, created_at, updated_at, users_id) VALUES (%(content)s, NOW(), NOW(), %(users_id)s);"
        return connectToMySQL("coding_dojo_wall").query_db(query, data)

    @classmethod
    def delete_post(cls, data):
        Comment.delete_post_comments(data)

        query2= """DELETE FROM posts WHERE id=%(post_id)s;"""
        connectToMySQL("coding_dojo_wall").query_db(query2, data)