import React from 'react';
import Sidebar from "../../components/Sidebar/Sidebar";
import Header from "../../components/Header/Header";
import Footer from "../../components/Footer/Footer";
import {Button} from 'react-bootstrap';
import styles from "./DocsPage.module.css";
export default function DocsPage({toggleSideBar, isSidebarOpen}) {
    return (
        <>
            <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSideBar}/>
            <section style={{height: "90vh"}}>
                <Header toggleSidebar={toggleSideBar}/>
                <div className="container-fluid">
                    <div className="d-flex justify-content-end mt-4">
                        <Button variant="primary">Загрузить файл</Button>
                    </div>
                    <div className="mt-4">
                        <h3>Документы и приказы</h3>
                        <ul>
                            <li>
                                <Button variant="link" href="https://www.mirea.ru/docs/264916/" download >
                                    <span className={styles.download_text}>Приказ "Об установлении размера платы за проживание в общежитиях РТУ МИРЭА"</span>
                                </Button>
                            </li>
                            <li>
                                <Button variant="link" href="https://www.mirea.ru/docs/178180/" download>
                                    <span className={styles.download_text}>Приказ о введении в действие Порядка предоставления мест в студенческих общежитиях...</span>
                                </Button>
                            </li>
                        </ul>
                    </div>
                </div>
            </section>
            <Footer/>
        </>
    );
}