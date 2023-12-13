import styles from "./DormList.module.css";

export default function DormList() {
    const dorms = [
        {
            id: 1,
            name: "Общежитие №1",
            img: null,
        },
        {
            id: 2,
            name: "Общежитие №2",
            img: null,
        },
        {
            id: 3,
            name: "Общежитие №3",
            img: null,
        },
    ]
    return (
        <>
            <div className={styles.dormListContainer}>
                <div className="d-flex flex-row flex-nowrap">
                    {dorms.map(item => (
                        <a href={`/dorms/${item.id}`}>
                            <div key={item.id} className={styles.card}>
                                {item.img && <img src={item.img} alt=""/>}
                                <div>{item.name}</div>
                            </div>
                        </a>
                    ))}
                </div>
            </div>
        </>
    )
}