from flask import Blueprint, render_template, request

posts_bp = Blueprint('posts', __name__, url_prefix="/posts")

@posts_bp.route("/create")
def create_post():
    return render_template("posts/create.html")

@posts_bp.route("/")
def list_posts():
    return render_template("posts/posts.html", posts=[])

