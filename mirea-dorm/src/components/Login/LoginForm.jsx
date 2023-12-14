import {Button, Form, Input} from "antd";
import {MailOutlined, LockOutlined, KeyOutlined} from "@ant-design/icons";
import mirea_logo from '../../assets/mirea_logo.png'
import styles from './LoginForm.module.css'

export default function LoginForm() {

    return (
        <div className="flex justify-content-center align-content-center">
            <div>
                <img src={mirea_logo} alt="РТУ МИРЭА" className={`${styles.auth_logo}`}/>
                <h1 className="text-center">Общежитие.Мирэа</h1>
                <hr/>
                <h3 className="text-center mb-4">Авторизация</h3>
            </div>

            <Form
                name="login"
                className={styles.login_form}
            >
            <Form.Item
                    name="email"
                    rules={[{required: true, message: 'Пожалуйста, введите email в домене @edu.mirea.ru или @mirea.ru!'}]}
                >
                    <Input prefix={<MailOutlined/>} placeholder="Email (edu.mirea.ru или mirea.ru)" type="email"/>
                </Form.Item>
                <Form.Item
                    name="password"
                    rules={[{required: true, message: 'Пожалуйста, введите пароль!'}]}
                >
                    <Input prefix={<KeyOutlined />} placeholder="Пароль" type="password"/>
                </Form.Item>
                <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
                    <Button type="primary" htmlType="submit" className="d-flex align-items-center">
                        <LockOutlined /> Войти
                    </Button>
                </Form.Item>
            </Form>

        </div>
    )

}