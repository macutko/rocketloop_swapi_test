import {axiosInstance} from "../lib/axiosInstance";
import {AxiosResponse} from "axios";

export class CharacterService {


    static getFilteredPeople(token: string, filmName: string, page: number): Promise<AxiosResponse<any>> {
        return axiosInstance.get<ICharacter[]>("api/v1/people/name", {
            params: {
                query: "Luke"
            },
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });
    }
}

export interface ICharacter {
    name: string,
    films: string[]
    species: string[]
    starships: string[]
}