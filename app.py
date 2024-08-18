from flask import Flask, jsonify, request
import requests
from mydefinitions import *

app = Flask(__name__)

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

@app.route('/films/<int:film_id>', methods = ['GET'])
def get_films_stsh_ve(film_id):
  
  extra = request.args.get("extra")
  if extra:
    character_id = int(extra[-2])
    if int(character_id) == character_id:
      return stsh_ve_ch_film(film_id, character_id)
    else:
      return jsonify({"Error":"Give a number"})
  return only_stsh_vh(film_id)

if __name__ == "__main__":
  app.run(debug=True)