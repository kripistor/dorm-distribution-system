import styles from "./Schedule.module.css";

export default function Schedule() {
    const schedule = [
        {
            id: 1,
            institute: "Институт перспективных технологий и индустриального программирования",
            timeInterval: "13:00 - 15:00",
            color: "#FFD749"
        },
        {
            id: 2,
            institute: "Институт радиоэлектроники и информатики",
            timeInterval: "14:00 - 16:00",
            color: "rgb(181, 107, 255, 0.7)"
        },
        {
            id: 3,
            institute: "Институт искусственного интеллекта",
            timeInterval: "15:00 - 17:00",
            color: "#0AC800"
        },
        {
            id: 4,
            institute: "Институт кибернетики",
            timeInterval: "16:00 - 18:00",
            color: "#436CFF"
        },
        {
            id: 5,
            institute: "Институт космических систем",
            timeInterval: "17:00 - 19:00",
            color: "#FF0000"
        }
    ]


    return (
        <>
            <div className={styles.scheduleContainer}>
                <div className="d-flex flex-row flex-nowrap">
                    {schedule.map(item => (
                            <div key={item.id} className={styles.schedule_card} style={{backgroundColor: item.color}}>
                                <div className={styles.timeInterval}>{item.timeInterval}</div>
                                <div className={styles.institute}>{item.institute}</div>
                            </div>
                        )
                    )
                    }
                </div>
            </div>
        </>
    )
}