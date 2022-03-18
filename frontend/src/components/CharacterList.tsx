import React, {FunctionComponent, useContext, useEffect} from "react";
import {useQuery} from "react-query";
import {AxiosError, AxiosResponse} from "axios";
import {CharacterService, ICharacter} from "../services/CharacterService";
import {CAuth} from "../context/AuthContext";
import logger from "../lib/logger";
import {CharacterItem} from "./CharacterItem";
import {CircularProgress} from "@mui/material";

export const CharacterList: FunctionComponent<{ selectedFilm: string }> = (props) => {
    const {token} = useContext((CAuth));

    const {
        data,
        isLoading,
        error
    } = useQuery<unknown, AxiosError, AxiosResponse<ICharacter[]>>("characters", () => CharacterService.getFilteredPeople(token, props.selectedFilm, 0));

    useEffect(() => {
        logger.debug(data);
    }, [data]);

    return (
        props.selectedFilm == ""
            ?
            <h1>Select a film please</h1>
            :
            (
                isLoading ?
                    <CircularProgress/>
                    :
                    <CharacterItem data={data?.data[0]}/>

            )

    );
};