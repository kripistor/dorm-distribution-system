import styles from "./Header.module.css";

export default function Header({toggleSidebar}) {

    return (
        <div className={`container-fluid ${styles.header_border}`}>
            <header className={styles.header}>
                <button onClick={toggleSidebar}>
                    <svg className={styles.header_menu} xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                         width="100%"
                         height="100%">
                        <path fill="#000000" d="M3 6h18v1H3zm0 10h18v1H3zm0-5h18v1H3z"/>
                    </svg>
                </button>
                <a href="/" className={styles.header_logo}>
                    <span>ОБЩЕЖИТИЕ.МИРЭА</span>
                </a>

                <a href="#">
                    <svg className={styles.header_search} width="23" height="24" viewBox="0 0 23 24" fill="none"
                         xmlns="http://www.w3.org/2000/svg">
                        <g id="Frame">
                            <path fill="#000000" id="Vector"
                                  d="M9.07992 1.44C4.57805 1.44 0.919922 5.09813 0.919922 9.6C0.919922 14.1019 4.57805 17.76 9.07992 17.76C10.8612 17.76 12.5074 17.1863 13.8499 16.215L20.1649 22.515L21.5149 21.165L15.2749 14.91C16.5012 13.4813 17.2399 11.6269 17.2399 9.6C17.2399 5.09813 13.5818 1.44 9.07992 1.44ZM9.07992 2.4C13.0624 2.4 16.2799 5.61751 16.2799 9.6C16.2799 13.5825 13.0624 16.8 9.07992 16.8C5.09742 16.8 1.87992 13.5825 1.87992 9.6C1.87992 5.61751 5.09742 2.4 9.07992 2.4Z"/>
                        </g>
                    </svg>
                </a>
            </header>
        </div>
    )
}