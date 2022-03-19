import React, {FunctionComponent, useContext, useEffect} from "react";
import {useQuery} from "react-query";
import {AxiosError, AxiosResponse} from "axios";
import {CharacterService, ICharacterResponse} from "../services/CharacterService";
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
    } = useQuery<unknown, AxiosError, AxiosResponse<ICharacterResponse>>("characters",
        () => CharacterService.getFilteredPeople(token, props.selectedFilm, 0));

    useEffect(() => {
        logger.debug(props.selectedFilm);
        logger.debug(data);
    }, [data, props.selectedFilm]);

    return (
        isLoading ?
            <CircularProgress/>
            :
            <>
                {data?.data.results.map((character) => <CharacterItem key={character.name} data={character}/>)}
            </>

    );
};