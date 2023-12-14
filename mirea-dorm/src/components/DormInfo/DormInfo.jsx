import styles from "./DormInfo.module.css";
import DormScheme from "../DormScheme/DormScheme";


export default function DormInfo({spec}) {

    return (
        <>
            <div className={styles.dorm_card}>
                <p>Общежитие по адресу: <span className={styles.dorm_address}>{spec.address}</span></p>
                <div className={styles.dorm_gallery}>
                    {spec.photos.map((photo) => (
                        <img src={photo.image_url} alt="img1"/>
                    ))}
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
        <hr/>
                <h4>План этажа общежития:</h4>
                <DormScheme scheme={spec.scheme}/>
            </div>

        </>
    )
}