import Header from "../../components/Header/Header";
import Sidebar from "../../components/Sidebar/Sidebar";
import styles from "./MainPage.module.css";
import Schedule from "../../components/Schedule/Schedule";
import DormList from "../../components/DormList/DormList";
import DormStats from "../../components/DormStats/DormStats";
import Footer from "../../components/Footer/Footer";

const MainPage = ({toggleSideBar, isSidebarOpen}) => {
    return (
        <>
            <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSideBar}/>
            <section style={{marginBottom:"50px"}}>
                <Header toggleSidebar={toggleSideBar}/>
                <div className="container-fluid">
                    <h1 className={styles.main_header}>Главная</h1>
                    <h3 className={styles.margin_top_36}>Расписание</h3>
                    <Schedule/>
                    <h3 className={styles.margin_top_36}>Общежития</h3>
                    <DormList/>
                    <h3 className={styles.margin_top_36}>Статистика</h3>

                    <DormStats/>
                    {/*<h3 className={styles.margin_top_36}>Отчетность</h3>*/}
                </div>
            </section>
            <Footer/>
        </>
    )
}

export default MainPage;
