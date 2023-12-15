import Sidebar from "../../components/Sidebar/Sidebar";
import Header from "../../components/Header/Header";
import UsersTable from "../../components/UsersTable/UsersTable";

export default function UsersPage({toggleSideBar, isSidebarOpen}) {
    return (
        <>
            <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSideBar}/>
            <Header toggleSidebar={toggleSideBar}/>
            <section>
                <div>
                    <h1 className="ms-3">Список студентов</h1>
                    <UsersTable/>
                </div>
            </section>

        </>
    )
}