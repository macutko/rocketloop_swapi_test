import * as React from "react";
import {FunctionComponent, useEffect} from "react";
import Box from "@mui/material/Box";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import {FilmService} from "../services/FilmService";
import logger from "../lib/logger";

export const FilmSelect: FunctionComponent = () => {
    const [age, setAge] = React.useState("");

    const handleChange = (event: any): void => {
        setAge(event.target.value);
    };

    useEffect(() => {
        FilmService.getFilms().then(async (r) => {
            const res = await r.json();
            // logger.debug(res);
            setAge("");
        }).catch(e => {
            setAge("");
            // logger.error(e);
        });
    }, []);

    return (
        <Box sx={{marginTop: "20vh"}}>
            <FormControl fullWidth>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={age}
                    onChange={handleChange}
                    sx={{backgroundColor: "white"}}
                >
                    <MenuItem disabled value="">
                        <em>Choose a film</em>
                    </MenuItem>
                    <MenuItem value={10}>Ten</MenuItem>
                    <MenuItem value={20}>Twenty</MenuItem>
                    <MenuItem value={30}>Thirty</MenuItem>
                </Select>
            </FormControl>
        </Box>
    );
};