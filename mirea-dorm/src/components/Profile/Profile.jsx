import styles from "./Profile.module.css";

export default function Profile({profile}) {
    return (
        <>
            <div className="container-fluid">
                <h1 className={styles.card_heading}>Карточка студента</h1>
                <div className={styles.person_card}>
                    {/*    set profile image from data, if no image - placeholder*/}
                    <img className={styles.person_card_img}
                         src={profile.img ? profile.img : "https://cdn4.vectorstock.com/i/1000x1000/46/73/person-gray-photo-placeholder-man-material-design-vector-23804673.jpg"} alt="person_photo"/>
                    <div>
                        <div>
                            <strong>{profile.name}</strong>
                        </div>
                        <div className={styles.person_card_info}>

                            <div>Номер студенческого: <strong>{profile.card_number}</strong></div>
                            <div>Email: <strong>{profile.login}</strong></div>
                            <div>Дата рождения: <strong>{profile.birthdate}</strong></div>
                            <div>Пол: <strong>{profile.sex}</strong></div>
                            <div>Курс: <strong>{profile.course}</strong></div>
                            <div>Год приёма: <strong>{profile.yearAdmission}</strong></div>
                            <div>Дата зачисления: <strong>{profile.enrollmentDate}</strong></div>
                            <div>Номер приказа о зачислении: <strong>{profile.orderNumber}</strong></div>
                            <div>Номер приказа о заселении в общежитие: <strong>{profile.orderDormNumber ? profile.orderDormNumber : "Ожидает заселения"}</strong></div>
                            <div>Льготы: <strong>{profile.benefits}</strong></div>
                            <div>Общежитие: <strong>{profile.dormAddress}</strong></div>
                            <div>Корпус: <strong>{profile.dormBlock}</strong></div>
                            <div>Этаж: <strong>{profile.dormFloor}</strong></div>
                            <div>Комната: <strong>{profile.dormRoom}</strong></div>
                        </div>
                    </div>

                </div>
            </div>
        </>
    )
}