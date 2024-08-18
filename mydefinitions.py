from flask import Flask, jsonify, request
import requests
SWAPI_BASE_URL = "https://swapi.dev/api/"

# It is help searching for people by ID
def fech_data(id, endpoint):
  response = requests.get(f"{SWAPI_BASE_URL}{endpoint}/{id}")

  if response.status_code == 200:
    try:
      data = response.json()
      return data
    except ValueError:
      print("Error: Unable to parse JSON from response")
      return None

# Thisi s a help to find all data in a table
def search_by_what_and_id(where,what,get_back):
  arr = []
  for element_url in where:
    element_id = element_url.split('/')[-2]
    element_data = fech_data(element_id, what)
    if element_data:
      arr.append(element_data[get_back])
    
  return arr

# Using people serch and data from table
def residents_on_planets(planet_id):
    planet_data = fech_data(planet_id, "planets")
    if not planet_data:
      return jsonify({"Error":"Planet not found!"}), 404
    
    residents = search_by_what_and_id(planet_data['residents'],'people','name')

    return jsonify({"Planet": planet_data['name'],
                    "Residents": residents})

def same_in(arr1,arr2):
  result = []
  for e in arr1:
    for e2 in arr2:
      if e == e2:
        result.append(e)
  
  return result

# It is for extra in get_films_stsh_ve
def stsh_ve_ch_film(film_id,character_id):
  film_data = fech_data(film_id,"films")
  character_data = fech_data(character_id, "people")
  if not film_data:
    return jsonify({"Error":"Film not found!"})
  if not character_data:
    return jsonify({"Error":"Character not found!"})

  starships_in_film = search_by_what_and_id(film_data['starships'],'starships','name')
  vehicls_in_film = search_by_what_and_id(film_data['vehicles'],'vehicles','name')

  starships_of_charater = search_by_what_and_id(character_data['starships'],'starships','name')
  vehicles_of_charater = search_by_what_and_id(character_data['vehicles'],'vehicles','name')

  starships_ch_fm = same_in(starships_in_film,starships_of_charater)

  vehicles_ch_fm = same_in(vehicls_in_film,vehicles_of_charater)

  return jsonify({"Film": film_data['title'],
                  "Character": character_data['name'],
                  "Starships": starships_ch_fm,
                  "vehicles": vehicles_ch_fm})

# When extra is not used in get_films_stsh_ve
def only_stsh_vh(film_id):
  film_data = fech_data(film_id,"films")
  if not film_data:
    return jsonify({"ERROR":"Film not found"})
  
  starships_in_film = search_by_what_and_id(film_data['starships'],'starships','name')
  vehicls_in_film = search_by_what_and_id(film_data['vehicles'],'vehicles','name')

  return jsonify({"Film": film_data['title'],
                    "Starships": starships_in_film,
                    "vehicles": vehicls_in_film})