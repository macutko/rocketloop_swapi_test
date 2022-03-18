import {BASE_URL} from "../lib/constants";

export class AuthService {

    static login(name: string, passwd: string): Promise<Response> {
        const formBody = [];

        formBody.push(encodeURIComponent("username") + "=" + encodeURIComponent(name));
        formBody.push(encodeURIComponent("password") + "=" + encodeURIComponent(passwd));

        return fetch(`${BASE_URL}/token`, {
            method: "POST",
            headers: {
                "accept": "application/json",
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: formBody.join("&")
        });
    }
}