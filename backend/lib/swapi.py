import logging

import requests

BASE_URL = "https://swapi.dev/api"


class Swapi:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_films(self):
        try:
            r = requests.get(url=f'{BASE_URL}/films/')
        except ConnectionError:
            self.logger.error('Connection error on swapi get films')
            return {}

        if r.status_code == 200:
            return r.json()

        return {}

    def get_poeple(self):
        try:
            r = requests.get(url=f'{BASE_URL}/people')
        except ConnectionError:
            self.logger.error('Connection error on swapi get films')
            return {}

        if r.status_code == 200:
            return r.json()
        return {}
