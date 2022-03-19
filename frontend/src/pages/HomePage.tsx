import {Container} from "@mui/material";
import {LoginForm} from "../components/LoginForm";
import {FilmSelect} from "../components/FilmSelect";
import React, {FunctionComponent, useContext} from "react";
import {CAuth} from "../context/AuthContext";
import {CharacterList} from "../components/CharacterList";

export const HomePage: FunctionComponent = () => {
    const {token} = useContext(CAuth);
    const [selectedFilm, setSelectedFilm] = React.useState("");

    return (
        <Container>
            {
                token == "" ?
                    <LoginForm/>
                    :
                    <>
                        <FilmSelect selectedFilm={selectedFilm} setSelectedFilm={setSelectedFilm}/>
                        {
                            selectedFilm == ""
                                ?
                                <h1>Select a film please</h1>
                                :
                                <CharacterList selectedFilm={selectedFilm}/>
                        }
                    </>
            }

        </Container>
    );
};