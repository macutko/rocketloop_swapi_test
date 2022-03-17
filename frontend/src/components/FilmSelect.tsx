import * as React from "react";
import {FunctionComponent, useEffect} from "react";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
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
            logger.debug(res);
            setAge("");
        }).catch(e => {
            setAge("");
            logger.error(e);
        });
    }, []);

    return (
        <Box sx={{minWidth: 120}}>
            <FormControl fullWidth>
                <InputLabel id="demo-simple-select-label">Age</InputLabel>
                <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    value={age}
                    label="Age"
                    onChange={handleChange}
                >
                    <MenuItem value={10}>Ten</MenuItem>
                    <MenuItem value={20}>Twenty</MenuItem>
                    <MenuItem value={30}>Thirty</MenuItem>
                </Select>
            </FormControl>
        </Box>
    );
};