import click
from flask import Flask
from board.pages import bp

def create_app():
    app = Flask(__name__)

    # Mendaftarkan Blueprint
    app.register_blueprint(bp)

    # Mendaftarkan command init-db
    @app.cli.command("init-db")
    def init_db():
        click.echo("Database berhasil diinisialisasi.")

    return app
