import {axiosInstance} from "../lib/axiosInstance";
import {AxiosResponse} from "axios";

export class FilmService {


    static getFilms(token: string): Promise<AxiosResponse<any>> {
        return axiosInstance.get<IFilm[]>("api/v1/films", {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });
    }
}

export interface IFilm {
    title: string
    url: string
}