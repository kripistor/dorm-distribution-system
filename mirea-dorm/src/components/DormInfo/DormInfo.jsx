import styles from "./DormInfo.module.css";


export default function DormInfo({spec}) {

    return (
        <>
            <div className={styles.dorm_card}>
                <p>Общежитие по адресу: <span className={styles.dorm_address}>{spec.address}</span></p>
                <div className={styles.dorm_gallery}>
                    <img src="https://placehold.co/360x200" alt="img1"/>
                    <img src="https://placehold.co/360x200" alt="img1"/>
                    <img src="https://placehold.co/360x200" alt="img1"/>
                    <img src="https://placehold.co/360x200" alt="img1"/>
                    <img src="https://placehold.co/360x200" alt="img1"/>
                    <img src="https://placehold.co/360x200" alt="img1"/>
                </div>
                <div className={styles.dorm_info}>
                    <div className={styles.dorm_info_item}>
                        <p>Площадь — <span>{spec.living_area} м<sup>2</sup></span></p>
                    </div>
                    <div className={styles.dorm_info_item}>
                        <p>Вместимость — <span>{spec.living_capacity} человек</span></p>
                    </div>
                    <div className={styles.dorm_info_item}>
                        <span>{spec.description}</span>
                    </div>
                </div>
            </div>

        </>
    )
}