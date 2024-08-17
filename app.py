from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

SWAPI_BASE_URL = "https://swapi.dev/api/"

def fech_data(id, endpoint):
  response = requests.get(f"{SWAPI_BASE_URL}{endpoint}/{id}")
  if response.status_code == 200:
    return jsonify(response.json())
  else:
    return jsonify({"error":"Person cannot found!"}), 404

@app.route("/")
def home():
  return jsonify({"message":"You are at Home!"})

@app.route('/people/<int:id>', methods=['GET'])
def get_person(id):
  return fech_data(id,"people")

if __name__ == "__main__":
  app.run(debug=True)