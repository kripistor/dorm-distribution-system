import axios from "axios";

let serverPath = "";

serverPath = "https://api.mirea.hm4nx.ru/api/v1"


export default class UsersService {
    static async get_user_profiles() {
        return new Promise((resolve, reject) => {
            axios.get(`${serverPath}/user_profiles`).then((res) => {
                    resolve(res.data)
                }
            ).catch((err) => {
                    console.error(err)
                    reject(err)
                }
            )
        })
    }
    static async distribute_users({users_id, dorm_id}) {
        let data = JSON.stringify({
            "user_ids": users_id
        })
        let config= {
            method: 'post',
                maxBodyLength: Infinity,
                url: 'https://api.mirea.hm4nx.ru/api/v1/distributions/1',
                headers: {
                'Content-Type': 'application/json'
            },
            data : data
        }
        return new Promise((resolve, reject) => {
            axios.request(config).then((res) => {
                    resolve(res.data)
                }
            ).catch((err) => {
                    console.error(err)
                }
            )
        })
    }
}