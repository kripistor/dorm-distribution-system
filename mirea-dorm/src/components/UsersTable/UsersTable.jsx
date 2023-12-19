import React, {useEffect, useState} from 'react';
import {Button, Input, Table} from 'antd';
import {useFetching} from "../../hooks/UseFetching";
import UsersService from "../../api/UsersService";

export default function UsersTable() {
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);
    const [loading, setLoading] = useState(false);
    const [value, setValue] = useState('');
    const [users, setUsers] = useState([]);

    const [fetchingUsers, isUsersLoading, UsersError] = useFetching(async () => {
        let response = await UsersService.get_user_profiles();
        if (isUsersLoading) {
            setLoading(true)
        }
        console.log(response)
        // add key to each user from user_id
        response = response.map((user) => {
            user.key = user.user_id;
            user.isDistributed = user.room_distribution !== null ? "Да" : "Нет";
            user.room_id = user.room_distribution !== null ? user.room_distribution.room_id : "Не заселен";
            return user
        });

        setUsers(response)
        setDataSource(response)
        setLoading(false)
    });
    const [dataSource, setDataSource] = useState(users);
    useEffect(() => {
        fetchingUsers().catch(e => console.log(e))
    }, []);
    const usersCount = users.length;

    const FilterByNameInput = (
        <Input
            placeholder="Поиск по имени"
            value={value}
            onChange={e => {
                const currValue = e.target.value;
                console.log(currValue)
                setValue(currValue);
                if (currValue === '' || currValue === undefined) {
                    setDataSource(users);
                    return;
                }
                const filteredData = users.filter(entry =>
                    entry.name.toLowerCase().includes(currValue.toLowerCase())
                );
                setDataSource(filteredData);
            }}
        />
    );
    const start = () => {
        setLoading(true);
        // update users
        fetchingUsers().catch(e => console.log(e))
        // ajax request after empty completing
        setTimeout(() => {
            setSelectedRowKeys([]);
            setLoading(false);
        }, 1000);
    };
    const onSelectChange = (newSelectedRowKeys) => {
        console.log('selectedRowKeys changed: ', newSelectedRowKeys);
        setSelectedRowKeys(newSelectedRowKeys);
    };
    const rowSelection = {
        selectedRowKeys,
        onChange: onSelectChange,
    };
    const hasSelected = selectedRowKeys.length > 0;
    const sendToServer = async () => {
        let distibution = await UsersService.distribute_users({users_id: selectedRowKeys, dorm_id: 1})
        alert("Студенты успешно зачислены")
        setSelectedRowKeys([])
        //     reload users
        fetchingUsers().catch(e => console.log(e))
    };
    const columns = [
        {
            title: FilterByNameInput,
            dataIndex: 'name',
            key: '1'
        },
        {
            title: 'Курс',
            dataIndex: 'course',
            filtered: true,
            filterSearch: true,
            filters: [
                {
                    text: 1,
                    value: 1,
                },
                {
                    text: 2,
                    value: 2,
                },
                {
                    text: 3,
                    value: 3,
                },
                {
                    text: 4,
                    value: 4,
                },
            ],
            onFilter: (value, record) => record.course === value,
            width: "5%"
        },
        {
            title: 'Пол',
            dataIndex: 'gender',
            filtered: true,
            filterSearch: true,
            filters: [
                {
                    text: 'Мужской',
                    value: 'М',
                },
                {
                    text: 'Женский',
                    value: 'Ж',
                },
            ],
            onFilter: (value, record) => record.gender.includes(value),
            width: '5%'
        },
        {
            title: 'Номер студенческого',
            dataIndex: 'card_number',
        },
        {
            title: "Телефон",
            dataIndex: "phone"
        },
        {
            title: "Заселен",
            dataIndex: "isDistributed",
            filtered: true,
            filterSearch: true,
            filters: [
                {
                    text: 'Да',
                    value: 'Да',
                },
                {
                    text: 'Нет',
                    value: 'Нет',
                },
            ],
            onFilter: (value, record) => record.isDistributed.includes(value),
        },
        {
            title: "Комната",
            dataIndex: "room_id",
            filtered: true,
            filterSearch: true,
        }
    ];

    return (
        <>
            <div className="container-fluid">
                <div
                    style={{
                        marginBottom: 16,
                    }}
                >
                    <p>Всего студентов: {usersCount}</p>
                    <Button type="primary" onClick={start} loading={loading} style={{marginRight: "10px"}}>
                        Обновить
                    </Button>
                    <Button type="primary" onClick={sendToServer} disabled={!hasSelected} style={{marginRight: "10px"}}>
                        Зачислить
                    </Button>
                    <Button type="primary" variant="link" href="https://api.mirea.hm4nx.ru/api/v1/documents/generate_report">
                        Скачать отчет
                    </Button>
                    <span
                        style={{
                            marginLeft: 8,
                        }}
                    >
          {hasSelected ? `Selected ${selectedRowKeys.length} items` : ''}
        </span>
                    <button></button>
                </div>
                <Table rowSelection={rowSelection} columns={columns} dataSource={dataSource} loading={loading} scroll={
                    {y: 500}
                }/>
            </div>
        </>
    );
};
