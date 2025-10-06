from flask import Blueprint, render_template, request, url_for, redirect
from board.database import get_db

bp = Blueprint('posts', __name__)

@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "POST":
       author = request.form["author"] or "Anonymous"
       message = request.form["message"]

       if message:
           db = get_db()
           db.execute(
              "INSERT INTO posts (author, message) VALUES (?, ?)",
              (author, message)
           )
           db.commit()
           return redirect(url_for("posts.show"))

    return render_template("posts/create.html")

@bp.route("/posts")
def show():
    db = get_db()
    posts = db.execute(
        "SELECT author, message, created FROM posts ORDER BY created DESC"
    ).fetchall()
    return render_template("posts/posts.html", posts=posts)
