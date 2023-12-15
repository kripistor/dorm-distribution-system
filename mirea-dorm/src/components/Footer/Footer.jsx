import styles from "./Footer.module.css";
import mireaLogo from "../../assets/mirea_logo.png";
import React from "react";

export default function Footer() {
    return (
        <footer className={styles.footer}>
            <img src={mireaLogo} alt="" className={styles.mirea_logo}/>
            <div className={styles.contactInfo}>
                <p>Тел: +7 (499) 215-65-65</p>
                <p>Email: info@mirea.ru</p>
                <p>Адрес: пр. Вернадского, 78</p>
            </div>
        </footer>
    )
}