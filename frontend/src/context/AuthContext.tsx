import React, {createContext, Dispatch, FunctionComponent, SetStateAction, useState} from "react";

interface IAuth {
    setToken: Dispatch<SetStateAction<string>>
    token: string
}

export const CAuth = createContext<IAuth>({token: "", setToken: () => undefined});

export const AuthContext: FunctionComponent = (props) => {
    const [token, setToken] = useState<string>("");

    return (
        <CAuth.Provider value={{token: token, setToken: setToken}}>
            {props.children}
        </CAuth.Provider>
    );
};