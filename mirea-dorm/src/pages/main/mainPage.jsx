import Header from "../../components/Header/Header";
import Sidebar from "../../components/Sidebar/Sidebar";


const MainPage = ({toggleSideBar, isSidebarOpen}) => {
    return (
        <>
            <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSideBar}/>
            <section>
                <Header toggleSidebar={toggleSideBar}/>
                <div className="container-fluid bg-black text-white">
                    <div>
                        <div>
                            <h1>Mirea dorm manage</h1>
                        </div>
                    </div>
                </div>
            </section>

        </>
    )
}

export default MainPage;
