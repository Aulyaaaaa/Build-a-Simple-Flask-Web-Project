from flask import Flask

from board.pages import bp

def create_app():
  app = Flask(__name__)

  # Mendaftarkan Blueprint
  app.register_blueprint(pages.bp)
  return app
