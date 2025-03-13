import json
import random
import requests
from config import API_URL


def get_last_comics():
    response = requests.get(API_URL)
    response.raise_for_status()
    response = response.json()
    return response['num']


def get_comics():
    random_number = random.randint(0, get_last_comics())
    url = f'https://xkcd.com/{random_number}/info.0.json'

    response = requests.get(url)
    response.raise_for_status()
    data = response.json()


    with open('comics_database.json', 'w') as file:
        json.dump(data, file, indent=4)
        return data

