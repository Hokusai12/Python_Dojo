from dojo_wall_app.config.mysqlconnection import connectToMySQL
from dojo_wall_app.models.user import User


class Comment:
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.creator = None

    @classmethod
    def get_comments_for_post(cls, post):
        query = "SELECT * FROM comments JOIN posts_has_comments ON comments.id = posts_has_comments.comments_id JOIN users ON comments.users_id = users.id WHERE posts_has_comments.posts_id=%(post_id)s;"
        data = {
            "post_id": post.id
        }
        results = connectToMySQL("coding_dojo_wall").query_db(query, data)
        post_comments = []
        for comment_data in results:
            comment = cls(comment_data)
            author_data = {
                "id": comment_data["users.id"],
                "first_name": comment_data["first_name"],
                "last_name": comment_data["last_name"],
                "email": comment_data["email"],
                "pw_hash": comment_data["pw_hash"],
                "created_at": comment_data["users.created_at"],
                "updated_at": comment_data["users.updated_at"]
            }
            comment.creator = User(author_data)
            post_comments.append(comment)
        return post_comments

    @classmethod
    def save_comment(cls, data):
        query1 = "INSERT INTO comments (content, users_id, created_at, updated_at) VALUES (%(content)s, %(users_id)s, NOW(), NOW());"
        match_data = {
            "comments_id": connectToMySQL("coding_dojo_wall").query_db(query1, data),
            "posts_id": data["posts_id"]
        }
        query2 = "INSERT INTO posts_has_comments (comments_id, posts_id) VALUES (%(comments_id)s, %(posts_id)s);"
        connectToMySQL("coding_dojo_wall").query_db(query2, match_data)
        return match_data['comments_id']

    @classmethod
    def delete_post_comments(cls, post_id):
        comment_ids = []
        select_query = """SELECT comments_id FROM posts_has_comments WHERE posts_id=%(post_id)s;"""
        comment_ids = connectToMySQL("coding_dojo_wall").query_db(select_query, post_id)
        delete_match_query = """DELETE FROM posts_has_comments WHERE comments_id=%(comments_id)s;"""
        for comment_id in comment_ids:
            connectToMySQL("coding_dojo_wall").query_db(delete_match_query, comment_id)
            delete_comment_query = """DELETE FROM comments WHERE id=%(comments_id)s;"""
            connectToMySQL("coding_dojo_wall").query_db(delete_comment_query, comment_id)

