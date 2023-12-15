import React, {useEffect, useRef} from 'react';
import mireaLogo from '../../assets/mirea_logo.png'
import styles from "./Sidebar.module.css";
import {Link, Outlet} from "react-router-dom";


function Sidebar({isOpen, toggleSidebar}) {
    const sideBarRef = useRef(null)
    const navInteract = (open) => {
        if (!sideBarRef.current) return
        if (!open) {
            sideBarRef.current.style.width = "0"
            toggleSidebar()
        } else {
            sideBarRef.current.style.width = "300px"
        }
    }
    useEffect(() => {
        if (isOpen) navInteract(true)
    }, [isOpen]);
    const items = [
        (props) => <Link to="/" onClick={toggleSidebar} {...props}>Главная</Link>,
        // (props) => <Link to="/dorms" onClick={toggleSidebar} {...props}>Общежития</Link>,
        (props) => <Link to="#" onClick={toggleSidebar} {...props}>Размер платы</Link>,
        // (props) => <Link to="#" onClick={toggleSidebar} {...props}>Статистика</Link>,
        (props) => <Link to="#" onClick={toggleSidebar} {...props}>Отчётность</Link>,
        (props) => <Link to="/docs" onClick={toggleSidebar} {...props}>Документы</Link>,
        (props) => <Link to="/users" onClick={toggleSidebar} {...props}>Студенты</Link>,
        (props) => <Link to="/login" onClick={toggleSidebar} {...props}>Авторизация</Link>,
        (props) => <Link to="/users" onClick={toggleSidebar} {...props}>Поиск</Link>,
    ];
    return (
        <div>
            <div id="mySidenav" ref={sideBarRef}
                 className={`${styles.sidenav} fixed inset-y-0 left-0 z-50 transform transition-transform duration-300 
                 ${isOpen ? 'translate-x-0' : '-translate-x-full'} w-64 bg-gray-800 p-8`}
            >
                <div className={styles.sidenav_content}>
                    <img src={mireaLogo} alt="" className={styles.mirea_logo}/>
                    <h5 style={{"margin-bottom": "24px"}}>Меню</h5>
                    <div className={styles.links}>
                        {items.map((item, index) => {
                                return (
                                    <div key={index} className={styles.link}>
                                        {item()}
                                    </div>
                                )
                            }
                        )}
                    </div>
                    <a href="javascript:void(0)" className={styles.close_btn}
                       onClick={() => navInteract(false)}>&times;</a>
                    <Outlet/>
                </div>
            </div>
        </div>

    );
}

export default Sidebar;