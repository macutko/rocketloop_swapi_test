from typing import List, Dict, Union


class Sanitizers:

    @staticmethod
    def people(ppl: List[Union[Dict[str, str], Dict[str, List[str]]]]):
        return [Sanitizers.person(person) for person in ppl]

    @staticmethod
    def person(person):
        return {"name": person["name"],
                "species": Sanitizers.url(person['species'] if isinstance(person['species'], list) else []),
                "films": Sanitizers.url(person['films'] if isinstance(person['films'], list) else []),
                "starships": Sanitizers.url(person['starships'] if isinstance(person['starships'], list) else [])
                }

    @staticmethod
    def url(urls: List[str]):
        return [url.replace("https://swapi.dev/api/", "https://localhost:8000/api/v1/") for url in urls]

    @staticmethod
    def specie(specie):
        return {"name": specie["name"]}

    @staticmethod
    def films(films):
        return [Sanitizers.film(f) for f in films]

    @staticmethod
    def film(film):
        return {"title": film["title"]}

    @staticmethod
    def starship(starship):
        return {"name": starship["name"]}
