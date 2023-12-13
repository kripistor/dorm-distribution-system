import Sidebar from "../../components/Sidebar/Sidebar";
import Header from "../../components/Header/Header";
import Profile from "../../components/Profile/Profile";
import {useParams} from "react-router-dom";
import ProfileNotFound from "../../components/ProfileNotFound/ProfileNotFound";

export default function ProfilePage({toggleSideBar, isSidebarOpen}) {
    let {profile_id} = useParams()

    const profiles = [
        {
            id: 1,
            name: "Иванов Иван Иванович",
            card_number: 23064,
            login: "ivanov.i.i@edu.mirea.ru",
            birthdate: "01.01.2000",
            sex: "М",
            course: 2,
            yearAdmission: 2022,
            enrollmentDate: "10.09.2022",
            orderNumber: "D036",
            orderDormNumber: 58067,
            benefits: null,
            dormAddress: "г. Москва, пр. Вернадского, д. 78, корп. 1",
            dormBlock: 3,
            dormFloor: 4,
            dormRoom: 46,
            img: null
        },
        {
            id: 2,
            name: 'User 2',
            card_number: 23002,
            login: 'user2@edu.mirea.ru',
            birthdate: '01.01.2002',
            sex: 'M',
            course: 3,
            yearAdmission: 2022,
            enrollmentDate: '10.09.2022',
            orderNumber: 'D02',
            orderDormNumber: 58002,
            benefits: null,
            dormAddress: 'г. Москва, пр. Вернадского, д. 78, корп. 2',
            dormBlock: 3,
            dormFloor: 3,
            dormRoom: 3,
            img: null
        },
        {
            id: 3,
            name: 'User 3',
            card_number: 23003,
            login: 'user3@edu.mirea.ru',
            birthdate: '01.01.2003',
            sex: 'F',
            course: 4,
            yearAdmission: 2022,
            enrollmentDate: '10.09.2023',
            orderNumber: 'D03',
            orderDormNumber: 58003,
            benefits: null,
            dormAddress: 'г. Москва, пр. Вернадского, д. 78, корп. 3',
            dormBlock: 1,
            dormFloor: 4,
            dormRoom: 4,
            img: null
        },
        {
            id: 4,
            name: 'User 4',
            card_number: 23004,
            login: 'user4@edu.mirea.ru',
            birthdate: '01.01.2004',
            sex: 'M',
            course: 5, yearAdmission: 2022,
            enrollmentDate: '10.09.2024',
            orderNumber: 'D04',
            orderDormNumber: 58004,
            benefits: null,
            dormAddress: 'г. Москва, пр. Вернадского, д. 78, корп. 4',
            dormBlock: 2,
            dormFloor: 1,
            dormRoom: 5,
            img: null
        },
        {
            id: 5,
            name: 'User 5',
            card_number: 23005,
            login: 'user5@edu.mirea.ru',
            birthdate: '01.01.2005',
            sex: 'F',
            course: 1,
            yearAdmission: 2022,
            enrollmentDate: '10.09.2025',
            orderNumber: 'D05',
            orderDormNumber: 58005,
            benefits: null,
            dormAddress: 'г. Москва, пр. Вернадского, д. 78, корп. 5',
            dormBlock: 3,
            dormFloor: 2,
            dormRoom: 6,
            img: null
        },
        {
            id: 6,
            name: 'User 6',
            card_number: 23006,
            login: 'user6@edu.mirea.ru',
            birthdate: '01.01.2006',
            sex: 'M',
            course: 2,
            yearAdmission: 2022,
            enrollmentDate: '10.09.2026',
            orderNumber: 'D06',
            orderDormNumber: 58006,
            benefits: null,
            dormAddress: 'г. Москва, пр. Вернадского, д. 78, корп. 6',
            dormBlock: 1,
            dormFloor: 3,
            dormRoom: 7,
            img: null
        },
        {
            id: 7,
            name: 'User 7',
            card_number: 23007,
            login: 'user7@edu.mirea.ru',
            birthdate: '01.01.2007',
            sex: 'F',
            course: 3,
            yearAdmission: 2022,
            enrollmentDate: '10.09.2027',
            orderNumber: 'D07',
            orderDormNumber: 58007,
            benefits: null,
            dormAddress: 'г. Москва,пр. Вернадского, д. 78, корп. 7',
            dormBlock: 2,
            dormFloor: 4,
            dormRoom: 8,
            img: null
        },
        {
            id: 8,
            name: 'User 8',
            card_number: 23008,
            login: 'user8@edu.mirea.ru',
            birthdate: '01.01.2008',
            sex: 'M',
            course: 4,
            yearAdmission: 2022,
            enrollmentDate: '10.09.2028',
            orderNumber: 'D08',
            orderDormNumber: 58008,
            benefits: null,
            dormAddress: 'г. Москва, пр. Вернадского, д. 78, корп. 8',
            dormBlock: 3,
            dormFloor: 1,
            dormRoom: 9,
            img: null
        },
        {
            id: 9,
            name: 'User 9',
            card_number: 23009,
            login: 'user9@edu.mirea.ru',
            birthdate: '01.01.2009',
            sex: 'F',
            course: 5,
            yearAdmission: 2022,
            enrollmentDate: '10.09.2029',
            orderNumber: 'D09',
            orderDormNumber: 58009,
            benefits: null,
            dormAddress: 'г. Москва, пр. Вернадского, д. 78, корп. 9',
            dormBlock: 1,
            dormFloor: 2,
            dormRoom: 10,
            img: null
        },
        {
            id: 10,
            name: 'User 10',
            card_number: 23010,
            login: 'user10@edu.mirea.ru',
            birthdate: '01.01.20010',
            sex: 'M',
            course: 1,
            yearAdmission: 2022,
            enrollmentDate: '10.09.20210',
            orderNumber: 'D010',
            orderDormNumber: 58010,
            benefits: null,
            dormAddress: 'г. Москва, пр. Вернадского, д. 78, корп. 10',
            dormBlock: 2,
            dormFloor: 3,
            dormRoom: 11,
            img: null
        }
    ]
    const profile = profiles[profile_id - 1]
    return (
        <>
            <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSideBar}/>
            <section>
                <Header toggleSidebar={toggleSideBar}/>
                {profile ? <Profile profile={profile}/> : <ProfileNotFound/>}
            </section>

        </>
    )
}