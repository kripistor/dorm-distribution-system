import './App.css';
import {BrowserRouter, Route, Routes} from "react-router-dom"

import LoginPage from "./pages/login/LoginPage";
import DormPage from "./pages/Dorms/DormPage";
import MainPage from "./pages/main/mainPage";
import {useState} from "react";
import ProfilePage from "./pages/Profile/ProfilePage";


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
                <Route path="/profile/me" element={<ProfilePage toggleSideBar={toggleSidebar} isSidebarOpen={isSidebarOpen}/>}/>
                <Route path="/profile/:profile_id" element={<ProfilePage toggleSideBar={toggleSidebar} isSidebarOpen={isSidebarOpen}/>}/>
                <Route path="/dorms" element={<DormPage toggleSideBar={toggleSidebar} isSidebarOpen={isSidebarOpen}/>}/>
            </Routes>
        </BrowserRouter>
    );
}

export default App;
