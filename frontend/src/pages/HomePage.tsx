import {Container} from "@mui/material";
import {LoginForm} from "../components/LoginForm";
import {FilmSelect} from "../components/FilmSelect";
import React, {FunctionComponent, useContext} from "react";
import {CAuth} from "../context/AuthContext";

export const HomePage: FunctionComponent = () => {
    const {token} = useContext(CAuth);

    return (
        <Container>
            {
                token == "" ?
                    <LoginForm/>
                    :
                    <FilmSelect/>
            }

        </Container>
    );
};