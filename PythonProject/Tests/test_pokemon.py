import requests
import pytest

url =  ' https://api.pokemonbattle.ru/v2'
trainer_id = '18212'


def test_status_code():
    respons = requests.get(url = f'{url}/trainers')
    assert respons.status_code == 200

def test_trainer_name():
    respons_get = requests.get(url = f'{url}/trainers', params = {'trainer_id' : trainer_id})
    assert respons_get.json()["data"][0]['trainer_name'] == 'Василёк'