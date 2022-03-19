import * as React from "react";
import {Dispatch, FunctionComponent, SetStateAction, useContext, useEffect} from "react";
import Box from "@mui/material/Box";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import {FilmService, IFilm} from "../services/FilmService";
import {CAuth} from "../context/AuthContext";
import {useQuery} from "react-query";
import {CircularProgress, Container, MenuItem} from "@mui/material";
import {AxiosError, AxiosResponse} from "axios";

export const FilmSelect: FunctionComponent<{ selectedFilm: string, setSelectedFilm: Dispatch<SetStateAction<string>> }> = (props) => {
    const {selectedFilm, setSelectedFilm} = props;
    const {token, setToken} = useContext(CAuth);
    const {
        data,
        isLoading,
        error
    } = useQuery<unknown, AxiosError, AxiosResponse<IFilm[]>>("films", () => FilmService.getFilms(token));


    const handleChange = (event: any): void => {
        setSelectedFilm(event.target.value);
    };

    useEffect(() => {
        if (error && error.response && error.response.status == 401) {
            setToken("");
        }
    }, [error, setToken]);

    return (
        <Box sx={{marginTop: "20vh"}}>
            <FormControl fullWidth>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={selectedFilm}
                    onChange={handleChange}
                >
                    {
                        isLoading ?
                            <Container>
                                <CircularProgress/>
                            </Container>
                            :
                            null
                    }
                    {data?.data.map((film) => <MenuItem key={film.title}
                        value={film.url}>{film.title}</MenuItem>)}
                </Select>
            </FormControl>
        </Box>
    );
};