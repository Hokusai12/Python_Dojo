from dojo_wall_app import app
from dojo_wall_app.models.user import User
from dojo_wall_app.models.post import Post
from dojo_wall_app.models.comment import Comment
from flask import render_template, session, request, redirect, flash

@app.route("/wall_page")
def display_wall():
    return render_template("wall_page.html", user=User.get_user(session['user_id']), posts=Post.get_all_posts())

@app.route("/make_post", methods=["POST"])
def make_post():
    if len(request.form["content"]) == 0:
        flash("Post must have content", "post_flash")
        return redirect("/wall_page")

    data = {
        "content": request.form["content"],
        "users_id": request.form["users_id"]
    }
    Post.save_post(data)
    return redirect("/wall_page")

@app.route("/make_comment", methods=["POST"])
def make_comment():
    if len(request.form["content"]) == 0:
        flash("Comment must have content", "comment_flash")
        return redirect("/wall_page")

    data = {
        "users_id": request.form["user_id"],
        "posts_id": request.form["post_id"],
        "content": request.form["content"]
    }
    Comment.save_comment(data)
    return redirect("/wall_page")

@app.route("/delete_post", methods=["POST"])
def delete_post():
    print("Post ID:", request.form["post_id"])
    data = {
        "post_id": request.form["post_id"]
    }
    Post.delete_post(data)
    return redirect("/wall_page")