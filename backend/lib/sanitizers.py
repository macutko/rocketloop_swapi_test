from typing import List, Dict, Union


class Sanitizers:

    @staticmethod
    def people(ppl: List[Union[Dict[str, str], Dict[str, List[str]]]]):
        return [
            {"name": person["name"],
             "species": person["species"],
             "films": Sanitizers.url(person['films'] if isinstance(person['films'], list) else []),
             "starships": Sanitizers.url(person['starships'] if isinstance(person['starships'], list) else [])
             }
            for person in ppl]

    @staticmethod
    def url(urls: List[str]):
        return [url.replace("https://swapi.dev/api/", "https://localhost:8000/api/v1/") for url in urls]
