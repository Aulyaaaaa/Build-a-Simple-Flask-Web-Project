import os
from dotenv import load_dotenv
from flask import Flask
from board import pages, posts, database

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        DATABASE=os.getenv("DATABASE"),
        ENVIRONMENT=os.getenv("ENVIRONMENT"),
    )

    app.register_blueprint(pages.bp)
    app.register_blueprint(posts.bp)

    database.init_app(app)
    app.cli.add_command(database.init_db_command)

    return app
