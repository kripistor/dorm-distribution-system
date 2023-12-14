import styles from "./DormScheme.module.css";

export default function DormScheme({scheme}) {
    return (
        <>
            <div className="container-fluid">
                <div className={styles.scheme_image}>
                    <img src={scheme} alt=""/>
                </div>
            </div>
        </>
    )
}