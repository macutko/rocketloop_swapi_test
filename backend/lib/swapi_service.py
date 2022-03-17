import logging

import requests

BASE_URL = "https://swapi.dev/api"


class SwapiService:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_films(self):
        return self.__get_swapi('/films/')

    def get_film(self, film_id: int):
        return self.__get_swapi(f'/films/{film_id}')

    def get_people(self, page: int):
        return self.__get_swapi(f'/people/?page={page}')

    def get_person(self, person_id: int):
        return self.__get_swapi(f'/people/{person_id}/')

    def get_specie(self, specie_id):
        return self.__get_swapi(f'/species/{specie_id}/')

    def get_starship(self, starship_id: int):
        return self.__get_swapi(f'/starships/{starship_id}')

    def __get_swapi(self, path: str):
        try:
            r = requests.get(url=f'{BASE_URL}{path}')
        except ConnectionError:
            self.logger.error(f'Connection error on {path}')
            return {}

        if r.status_code == 200:
            return r.json()
        return {}
