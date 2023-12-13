import styles from "./ProfileNotFound.module.css";

export default function ProfileNotFound() {
    return (
        <div className={styles.container}>
            <h1 className={styles.message}>Профиль не найден!</h1>
            <p>Попробуйте ввести другой номер карточки</p>
        </div>
    )
}