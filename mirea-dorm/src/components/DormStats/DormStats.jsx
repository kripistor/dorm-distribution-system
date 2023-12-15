import BatteryIndicator from "../BatteryIndicator/BatteryIndicator";
import styles from "./DormStats.module.css";
import {useState} from "react";

export default function DormStats() {
    const dorms = [
        {
            "dorm_id": 1,
            "dorm_name": "Общежитие на Юго-Западной",
            "dorm_address": "проспект Вернадского, дом 86, стр.1",
            "occupied_space": 4,
            "total_space": 52,
            "floors": [
                {
                    "floor_id": 1,
                    "floor_name": "3",
                    "occupied_space": 4,
                    "total_space": 16,
                    "rooms_free": 4
                },
                {
                    "floor_id": 3,
                    "floor_name": "3",
                    "occupied_space": 0,
                    "total_space": 12,
                    "rooms_free": 2
                },
                {
                    "floor_id": 2,
                    "floor_name": "3",
                    "occupied_space": 0,
                    "total_space": 24,
                    "rooms_free": 4
                }
            ]
        }
    ]

    const [isShown, setIsShown] = useState(new Array(dorms.length).fill(false));
    return (
        <>
            <div className={styles.dormStatsContainer}>
                <div className="d-flex flex-row flex-nowrap">
                    {dorms.map((item, index) => (
                        <>
                            <div className={styles.dorm_stats}>
                                <div className={styles.dorm_card}
                                     onMouseOver={() => {
                                         const newIsShown = [...isShown];
                                         newIsShown[index] = true;
                                         setIsShown(newIsShown);
                                     }}
                                     onMouseLeave={() => {
                                         const newIsShown = [...isShown];
                                         newIsShown[index] = false;
                                         setIsShown(newIsShown);
                                     }}>
                                    <BatteryIndicator key={item.dormId}
                                                      percent={item.occupied_space / item.total_space * 100}/>
                                    <p style={{textAlign: "center"}}>Статистика
                                        заселения<br/>{item.dorm_name}</p>

                                </div>
                                <div className={styles.tooltip}>
                                    {item.floors.map((floor, floorIndex) => (
                                        <div key={floorIndex} className={styles.stats_card}>
                                            <BatteryIndicator percent={floor.occupied_space / floor.total_space * 100}/>
                                            <div>
                                                <p className={styles.stats_card_heading}>Заселение {floorIndex + 1} этажа</p>
                                                <p className={styles.stats_card_value}>(Осталось комнат - {floor.rooms_free})</p>
                                            </div>

                                        </div>
                                    ))}
                                </div>
                            </div>


                        </>

                    ))}
                </div>
            </div>
        </>
    )
}