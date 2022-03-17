import logging
from typing import List, Optional

import requests
from pydantic import BaseModel

from lib.custom_typings import URL

BASE_URL = "https://swapi.dev/api"


class SwapiService:

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_films(self):
        return self.__get_swapi('/films/')

    def get_people(self, page: int):
        return self.__get_swapi(f'/people/?page={page}')

    def get_species(self, page: int):
        return self.__get_swapi(f'/species/?page={page}')

    def get_vehicles(self, page: int):
        return self.__get_swapi(f'/species/?page={page}')

    def __get_swapi(self, path: str):
        try:
            r = requests.get(url=f'{BASE_URL}{path}')
        except ConnectionError:
            self.logger.error(f'Connection error on {path}')
            return {}

        if r.status_code == 200:
            return r.json()
        return {}


class Person(BaseModel):
    name: Optional[Optional[str]]
    height: Optional[str]
    mass: Optional[str]
    hair_color: Optional[str]
    skin_color: Optional[str]
    eye_color: Optional[str]
    birth_yer: Optional[str]
    gender: Optional[str]
    homeworld: Optional[URL]
    films: Optional[List[URL]]
    species: Optional[List[URL]]
    vehicles: Optional[List[URL]]
    starships: Optional[List[URL]]
    created: Optional[str]
    edited: Optional[str]
    url: Optional[URL]
