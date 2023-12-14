import styles from "./Footer.module.css";
import mireaLogo from "../../assets/mirea_logo.png";
import React from "react";

export default function Footer() {
    return (
        <footer className={styles.footer}>
            <img src={mireaLogo} alt="" className={styles.mirea_logo}/>
            <div className={styles.contactInfo}>
                <p>Tel: +1 234 567 890</p>
                <p>Email: info@example.com</p>
                <p>Address: 1234 Street, City, Country</p>
            </div>
        </footer>
    )
}