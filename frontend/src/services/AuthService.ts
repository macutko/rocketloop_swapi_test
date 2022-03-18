import {axiosInstance} from "../lib/axiosInstance";
import {AxiosResponse} from "axios";

export class AuthService {

    static login(name: string, passwd: string): Promise<AxiosResponse<any>>{
        const formBody = [];

        formBody.push(encodeURIComponent("username") + "=" + encodeURIComponent(name));
        formBody.push(encodeURIComponent("password") + "=" + encodeURIComponent(passwd));

        return axiosInstance.post("/token", formBody.join("&"), {
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        });
    }
}