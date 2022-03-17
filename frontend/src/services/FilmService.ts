import {BASE_URL} from "../lib/constants";

export class FilmService {


    static getFilms(): Promise<Response> {
        return fetch(`${BASE_URL}/api/v1/films`);
    }
}