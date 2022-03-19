import React, {FunctionComponent} from "react";
import {ICharacter} from "../services/CharacterService";

export const CharacterItem: FunctionComponent<{ data: ICharacter | undefined }> = (props) => {

    return (
        <h1>
            {props.data?.name}
        </h1>
    );
};