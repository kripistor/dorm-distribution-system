import './App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom"

import LoginPage from "./pages/login/LoginPage";
import DormPage from "./pages/Dorms/DormPage";
import MainPage from "./pages/main/mainPage";
import {useState} from "react";


function App() {
    const [isSidebarOpen, setSidebarOpen] = useState(false);

    const toggleSidebar = () => {
        setSidebarOpen(!isSidebarOpen);
    };
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<MainPage toggleSideBar={toggleSidebar} isSidebarOpen={isSidebarOpen}/>}/>
                <Route path="/login" element={<LoginPage/>}/>
                <Route path="/dorms" element={<DormPage toggleSideBar={toggleSidebar} isSidebarOpen={isSidebarOpen}/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
