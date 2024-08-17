from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

SWAPI_BASE_URL = "https://swapi.dev/api/"

@app.route("/")
def home():
  return jsonify({"message":"You are at Home!"})

@app.route('/people/<int:id>', methods=['GET'])
def get_person(id):
  response = requests.get(f"{SWAPI_BASE_URL}people/{id}/")
  if response.status_code == 200:
    return jsonify(response.json())
  else:
    return jsonify({"error":"Person cannot found!"}), 404

if __name__ == "__main__":
  app.run(debug=True)