import BatteryIndicator from "../BatteryIndicator/BatteryIndicator";
import styles from "./DormStats.module.css";
import {useState} from "react";

export default function DormStats() {
    const dorms = [
        {
            dorm_id: 1,
            dorm_name: "Общага 1",
            dorm_address: "проспект Вернадского, дом 86, ст",
            occupied_space: 4,
            total_space: 19,
            floors: [
                {
                    floor_id: 1,
                    floor_name: "1 этаж",
                    occupied_space: 4,
                    total_space: 10,
                    rooms_free: 2
                },
                {
                    floor_id: 3,
                    floor_name: "2 этаж",
                    occupied_space: 0,
                    total_space: 7,
                    rooms_free: 2
                },
                {
                    floor_id: 4,
                    floor_name: "3 этаж",
                    occupied_space: 0,
                    total_space: 50,
                    rooms_free: 1,
                }
            ]
        },
        {
            dormId: 2,
            dormName: "Общежитие №2",
            occupied_space: 500,
            total_space: 2000,
            floors: [
                {
                    floorId: 1,
                    floor_name: 1,
                    occupied_space: 200,
                    total_space: 500,
                    rooms_free: 10,
                },
                {
                    floorId: 2,
                    floor_name: 2,
                    occupied_space: 150,
                    total_space: 500,
                    rooms_free: 10,
                },
                {
                    floorId: 3,
                    floor_name: 3,
                    occupied_space: 150,
                    total_space: 500,
                    rooms_free: 10,
                }
            ]
        },
        {
            dormId: 3,
            dormName: "Общежитие №3",
            occupied_space: 1500,
            total_space: 2000,
            floors: [
                {
                    floorId: 1,
                    floor_name: 1,
                    occupied_space: 200,
                    total_space: 500,
                    rooms_free: 1,
                },
                {
                    floorId: 2,
                    floor_name: 2,
                    occupied_space: 50,
                    total_space: 500,
                    rooms_free: 10,
                },
                {
                    floorId: 3,
                    floor_name: 3,
                    occupied_space: 150,
                    total_space: 500,
                    rooms_free: 5,
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
                                        заселения<br/>{item.dormName}</p>

                                </div>
                                <div className={styles.tooltip}>
                                    {item.floors.map((floor, floorIndex) => (
                                        <div key={floorIndex} className={styles.stats_card}>
                                            <BatteryIndicator percent={floor.occupied_space / floor.total_space * 100}/>
                                            <div>
                                                <p className={styles.stats_card_heading}>Заселение {floorIndex + 1} этажа</p>
                                                <p className={styles.stats_card_value}>(Осталось {floor.rooms_free} комнат)</p>
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