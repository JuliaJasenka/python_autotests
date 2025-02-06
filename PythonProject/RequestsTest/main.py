import requests

url =  ' https://api.pokemonbattle.ru/v2'
header = {'Content-Type' : 'application/json',
          'trainer_token' : 'd471adc7e140475cc998ea9658d74fca'}
body_pokemon = {
    "name": "generate",
    "photo_id": -1
}

body_newName = {
    "pokemon_id": "223493",
    "name": "New Name",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": "223481"
}

#response = requests.post(url = f'{url}/pokemons', headers = header, json = body_pokemon)
#print(response.text)

#response_newName = requests.put(url = f'{url}/pokemons', headers = header, json = body_newName)
#print(response_newName.text)

response_pokeball = requests.post(url = f'{url}/trainers/add_pokeball', headers = header, json = body_pokeball)
print(response_pokeball.text)

