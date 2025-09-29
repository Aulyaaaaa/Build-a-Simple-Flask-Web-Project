from flask import Flask

def create_app():
  app = Flask(__name__)
  
  from board.posts import posts_bp
  from board.pages import pages_bp

  app.register_blueprint(posts_bp)
  app.register_blueprint(pages_bp)
 
  return app 
