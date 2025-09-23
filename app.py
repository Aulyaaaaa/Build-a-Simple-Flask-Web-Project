from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
 return "Hell0, World!"

if__name__=="__main__":
  app.run(host="0.0.0.0",port=8000, debug=True)
