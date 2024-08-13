from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return "You are at Home!"

if __name__ == "__main__":
  app.run(debug=True)