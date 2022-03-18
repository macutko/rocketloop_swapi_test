import React, {FunctionComponent} from "react";
import {AuthContext} from "../context/AuthContext";
import {HomePage} from "../pages/HomePage";
import {QueryClient, QueryClientProvider} from "react-query";

const App: FunctionComponent = () => {
    const queryClient = new QueryClient();

    return (
        <AuthContext>
            <QueryClientProvider client={queryClient}>
                <HomePage/>
            </QueryClientProvider>
        </AuthContext>
    );
};

export default App;
