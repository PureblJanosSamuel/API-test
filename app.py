from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

SWAPI_BASE_URL = "https://swapi.dev/api/"

def fech_data(id, endpoint):
  response = requests.get(f"{SWAPI_BASE_URL}{endpoint}/{id}")

  if response.status_code == 200:
    try:
      data = response.json()
      return data
    except ValueError:
      print("Error: Unable to parse JSON from response")
      return None
  
def residents_on_planets(planet_id):
    planet_data = fech_data(planet_id, "planets")
    if not planet_data:
      return jsonify({"Error":"Planet not found!"}), 404
    
    residents = []

    for resident_url in planet_data['residents']:
      resident_id = resident_url.split('/')[-2]
      resident_data = fech_data(resident_id,'people')
      if resident_data:
        residents.append(resident_data['name'])

    return jsonify({"Planet": planet_data['name'],
                    "Residents": residents})
      

@app.route("/")
def home():
  return jsonify({"message":"You are at Home!"})

@app.route('/people/<int:id>', methods=['GET'])
def get_person(id):
  return fech_data(id,"people")

@app.route('/planets/<int:id>', methods=['GET'])
def get_planet(id):
  return fech_data(id,"planets")

@app.route('/planets/<int:planet_id>/residents', methods = ['GET'])
def get_planet_residents(planet_id):
  return residents_on_planets(planet_id)

if __name__ == "__main__":
  app.run(debug=True)