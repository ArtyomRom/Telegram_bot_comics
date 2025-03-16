import random
import requests
from config import API_URL


def get_last_comic():
    latest_comic = requests.get(API_URL)
    latest_comic.raise_for_status()
    latest_comic = latest_comic.json()
    return latest_comic['num']


def get_comic():
    random_number = random.randint(1, get_last_comic())
    url = f'https://xkcd.com/{random_number}/info.0.json'
    comic_book_information = requests.get(url)
    comic_book_information.raise_for_status()
    comic_book_information = comic_book_information.json()
    return comic_book_information
