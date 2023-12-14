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
        return new Promise((resolve, reject) => {
            axios.post(`${serverPath}/user_profiles/distribute/${dorm_id}`, {user_ids: users_id}).then((res) => {
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