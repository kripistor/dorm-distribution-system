import axios from "axios";

let serverPath = "";

serverPath = "https://api.mirea.hm4nx.ru/api/v1"


export default class DormService {

    static async get_dorms() {
        return new Promise((resolve, reject) => {
            axios.get(`${serverPath}/dormitories`).then((res) => {
                    resolve(res.data)
                }
            ).catch((err) => {
                    console.error(err)
                    reject(err)
                }
            )
        })
    }

    static async get_dorm_by_id(dorm_id) {
        return new Promise((resolve, reject) => {
            axios.get(`${serverPath}/dormitories/${dorm_id}`).then((res) => {
                    resolve(res.data)
                }
            ).catch((err) => {
                    console.error(err)
                    reject(err)
                }
            )
        })
    }

    static async get_dorm_stats_by_id(dorm_id) {
        return new Promise((resolve, reject) => {
            axios.get(`${serverPath}/dormitories/stats/${dorm_id}`).then((res) => {
                    resolve(res.data)
                }
            ).catch((err) => {
                    console.error(err)
                    reject(err)
                }
            )
        })
    }
}