from flask import Blueprint, render_template, redirect, url_for

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
 return redirect(url_for("posts.create"))

@bp.route("/about")
def about():
 return render_template("pages/about.html")

@bp.route("/contact")
def contact():
    return render_template("pages/contact.html")
