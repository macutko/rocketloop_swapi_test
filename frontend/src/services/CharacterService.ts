import {axiosInstance} from "../lib/axiosInstance";
import {AxiosResponse} from "axios";

export class CharacterService {


    static getFilteredPeople(token: string, filmName: string, page: number): Promise<AxiosResponse<any>> {
        return axiosInstance.get<ICharacter[]>("api/v1/people/films", {
            params: {
                query: filmName
            },
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });
    }
}

export interface ICharacterResponse {
    next: string,
    results: ICharacter[]
}

export interface ICharacter {
    name: string,
    films: string[]
    species: string[]
    starships: string[]
}