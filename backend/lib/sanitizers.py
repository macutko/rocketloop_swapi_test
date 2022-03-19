from typing import List, Dict, Union


class Sanitizers:

    @staticmethod
    def people(ppl: List[Union[Dict[str, str], Dict[str, List[str]]]]):
        return [Sanitizers.person(person) for person in ppl]

    @staticmethod
    def person(person):
        return {"name": person["name"],
                "species": Sanitizers.urls(person['species'] if isinstance(person['species'], list) else []),
                "films": Sanitizers.urls(person['films'] if isinstance(person['films'], list) else []),
                "starships": Sanitizers.urls(person['starships'] if isinstance(person['starships'], list) else [])
                }

    @staticmethod
    def urls(urls: List[str]):
        return [Sanitizers.url(url) for url in urls]

    @staticmethod
    def url(url: str):
        return url.replace("https://swapi.dev/api/", "http://localhost:8000/api/v1/")

    @staticmethod
    def specie(specie):
        return {"name": specie["name"]}

    @staticmethod
    def films(films):
        return [Sanitizers.film(f) for f in films]

    @staticmethod
    def film(film):
        return {"title": film["title"], "url": Sanitizers.url(film["url"])}

    @staticmethod
    def starship(starship):
        return {"name": starship["name"]}
