from flask import Blueprint, render_template, request

bp = Blueprint('posts', __name__, url_prefix="/posts")

@bp.route("/create")
def create_post():
    return render_template("posts/create.html")

@bp.route("/")
def list_posts():
    return render_template("posts/posts.html", posts=[])

