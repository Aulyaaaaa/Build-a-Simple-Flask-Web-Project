from flask import Blueprint, render_template, redirect, url_for

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/")
def home():
 return redirect(url_for("posts.create_post"))

@pages_bp.route("/about")
def about():
 return render_template("pages/about.html")

@pages_bp.route("/contact")
def contact():
    return render_template("pages/contact.html")
