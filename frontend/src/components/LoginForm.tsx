import React, {FunctionComponent, useContext, useState} from "react";
import {Button, Container, TextField} from "@mui/material";
import {CAuth} from "../context/AuthContext";
import {AuthService} from "../services/AuthService";
import useIsMounted from "../hooks/isMounted";

export const LoginForm: FunctionComponent = () => {
    const [name, setName] = useState<string>("");
    const [passwd, setPasswd] = useState<string>("");
    const {setToken} = useContext(CAuth);
    const isMounted = useIsMounted();

    const submitForm = (event: any): void => {
        event.preventDefault();

        AuthService.login(name, passwd).then(async (res) => {
            const response = await res.json();
            if (isMounted()) {
                setToken(response?.access_token);
            }
        });
    };

    return (
        <form onSubmit={submitForm}>
            <Container sx={{marginTop: "20vh"}}>
                <TextField
                    fullWidth
                    color="primary"
                    id="filled-username-input"
                    label="Username"
                    type="name"
                    onChange={(e): void => setName(e.target.value)}
                    value={name}
                    autoComplete="current-password"
                    variant="outlined"
                    sx={{marginBottom: "2vh"}}
                />
                <TextField
                    fullWidth
                    id="filled-password-input"
                    label="Password"
                    type="password"
                    onChange={(e): void => setPasswd(e.target.value)}
                    value={passwd}
                    autoComplete="current-password"
                    variant="outlined"
                    sx={{marginBottom: "2vh"}}
                />
                <Button variant="contained" sx={{width: "100%"}} type={"submit"}>Login</Button>
            </Container>
        </form>
    );
};