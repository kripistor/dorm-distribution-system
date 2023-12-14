import DormInfo from "../../components/DormInfo/DormInfo";
import styles from "../../components/DormInfo/DormInfo.module.css"
import Sidebar from "../../components/Sidebar/Sidebar";
import Header from "../../components/Header/Header";
import {useParams} from "react-router-dom";
import {useEffect, useState} from "react";
import {useFetching} from "../../hooks/UseFetching";
import DormService from "../../api/DormService";

const DormPage = ({toggleSideBar, isSidebarOpen}) => {
    const dorm_id = useParams().id;
    const [dorm, setDorm] = useState([]);
    const [fetchingDorm, isDormLoading, DormError] = useFetching(async () => {
        let response = await DormService.get_dorm_by_id(dorm_id);
        console.log(response)
        setDorm(response)
    });
    useEffect(() => {
        fetchingDorm().catch(e => console.log(e))
    }, [dorm_id]);
    const spec =
        {
            "id": 1,
            "address": "г. Москва, проспект Вернадского, дом 86, стр.1 (ближайшая станция метро: Юго-Западная)",
            "living_area": 8359.6,
            "living_capacity": 1161,
            "description": "Общежитие представляет собой 14-этажное панельное здание.\n" +
                "Общежитие блочного типа – раздельные комнаты, расположенные блоками (по 2 комнаты) с отдельным санитарным узлом и душевой комнатой. Кухня на этаже.\n" +
                "Общежитие оборудовано системой видеонаблюдения; пожарной сигнализацией.\n" +
                "В каждой комнате имеется: гардероб (на комнату); кровать (на каждого проживающего); тумбочка (на каждого проживающего); полка (на каждого проживающего); письменный стол (на комнату); стул (на каждого проживающего); розетки 220В; постельные принадлежности (на каждого проживающего): матрас, подушка, одеяло, покрывало, комплект постельного белья.\n" +
                "В общежитии есть комната для самоподготовки, велопарковка, чертежная комната, библиотека, комната занятий танцами, сеть интернет, постирочная комната, теннисный стол.",
            "photos": [
                {
                    "id": 1,
                    "image_url": "https://www.mirea.ru/upload/medialibrary/8fb/135sryym2nmww1taovif3jj494utisxg/20220912_DSC07535.jpg",
                },
                {
                    "id": 2,
                    "image_url": "https://www.mirea.ru/upload/medialibrary/7bd/ki6xk4lowsh15semt892055zpi26h45r/20220912_DSC07541.jpg",
                },
                {
                    "id": 3,
                    "image_url": "https://www.mirea.ru/upload/medialibrary/4d5/v2lsvfy6kp2fpmmko0r1dfmv1d5da8dp/20220912_DSC07573.jpg",
                },
                {
                    "id": 4,
                    "image_url": "https://www.mirea.ru/upload/medialibrary/4a5/i2bmqsksfw05u8pk61nzeaqvi0ji88by/20220912_DSC07576.jpg",
                },
                {
                    "id": 5,
                    "image_url": "https://www.mirea.ru/upload/medialibrary/183/8rlr4i4l37pj0g95u1qndrdh42mb4o6w/20220912_DSC07595.jpg",
                },
                {
                    "id": 6,
                    "image_url": "https://www.mirea.ru/upload/medialibrary/2dc/g2vinp1ovxtocxi9mmsml365yp23qyq4/20220919_DSC08921.jpg",
                },
            ],
            "scheme": "https://andrometa.ru/assets/images/zdaniya-dlya-zhizni/obekty/gostinicy/obshhezhitie-na-49-komnat/__3.jpg"
        }


    return (
        <>
            <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSideBar}/>
            <section>
                <Header toggleSidebar={toggleSideBar}/>

                <div className={`container-fluid ${styles.dorms_list}`}>
                    <DormInfo spec={spec}/>
                </div>
            </section>
        </>
    )
}

export default DormPage;
