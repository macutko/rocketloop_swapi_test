import React, {FunctionComponent} from "react";
import {AuthContext} from "../context/AuthContext";
import {HomePage} from "../pages/HomePage";

const App: FunctionComponent = () => {

    return (
        <AuthContext>
            <HomePage/>
        </AuthContext>
    );
};

export default App;
