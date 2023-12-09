import './App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom"
import MainPage from "./pages/main/mainPage";
import LoginPage from "./pages/login/LoginPage";


function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<MainPage/>}/>
                <Route path="/login" element={<LoginPage/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
