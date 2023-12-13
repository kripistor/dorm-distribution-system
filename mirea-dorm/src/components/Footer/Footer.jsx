import styles from "./Footer.module.css";
import mireaLogo from "../../assets/mirea_logo.png";
import React from "react";

export default function Footer() {
    return (
        <>
            <footer>
                <img src={mireaLogo} alt="" className={styles.mirea_logo}/>

            </footer>
        </>
    )
}