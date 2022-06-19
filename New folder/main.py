import sqlite3
import re


class database:


 #  функция создания таблиц
    def start():
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute("""PRAGMA foreign_keys=on;""")
        conn.commit()

        curs.execute("""CREATE TABLE IF NOT EXISTS users (
            user_id INT NOT NULL PRIMARY KEY,
            time_user TEXT,
            money TEXT,
            warns TEXT,
            mutes TEXT,
            role_id TEXT NOT NULL,
            FOREIGN KEY (role_id) REFERENCES roles(id)
            ) """)
        conn.commit()

        curs.execute("""CREATE TABLE IF NOT EXISTS roles (
            id TEXT NOT NULL PRIMARY KEY,
            name TEXT,
            cost TEXT,
            time_role TEXT,
            creator TEXT
            ) """)
        conn.commit()

 ############################################################################################################################################################ добавление пользователя
 #  аргумент user_id - айди пользователя (его номер)
 #  аргумент time_user - время добавления пользователя на сервер (формат даты - SS-MM-HH DD-MM-YYYY)

    def add_new_user(user_id, time_user):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"INSERT INTO users (user_id, time_user, money, warns, mutes, role_id) VALUES ('{user_id}', '{time_user}', '0', '0', '0', '0')")
        conn.commit()        

 ################################################################################################### проверки:

 #проверка времени регистрации пользователя, возвращает дату регистрации пользователя (формат даты - SS-MM-HH DD-MM-YYYY)

    def check_time(user_id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"SELECT time_user FROM users WHERE user_id = '{user_id}'")
        return str(re.findall(r"\d{2}-\d{2}-\d{2} \d{2}-\d{2}-\d{4}", str(curs.fetchone())))

 #проверка колличества money пользователя, возвращает число

    def check_money(user_id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"SELECT money FROM users WHERE user_id = '{user_id}'")
        return re.sub("[^0-9]", "", str(curs.fetchone()))

 #проверка колличества варнов, возвращает цифру - колличество варнов

    def check_warn(user_id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"SELECT warns FROM users WHERE user_id = '{user_id}'")
        return re.sub("[^0-9]", "", str(curs.fetchone()))

 #проверка времени mute пользователя, возвращает дату окончания mute (формат даты - SS-MM-HH DD-MM-YYYY)

    def check_mute(user_id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"SELECT mutes FROM users WHERE user_id = '{user_id}'")
        return re.findall(r"\d{2}-\d{2}-\d{2} \d{2}-\d{2}-\d{4}", str(curs.fetchone()))

 #проверка role_id пользователя (проверка привязанных к пользователю ролей)

    def check_role_id(user_id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"SELECT role_id FROM users WHERE user_id = '{user_id}'")
        return re.sub("[^0-9]", "", str(curs.fetchone()))

 ################################################################################################### изменения:

 #изменение money (колличества денег) у пользователя

    def set_money(user_id, money):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f" UPDATE users SET money = '{money}' WHERE user_id = '{user_id}'")
        conn.commit()

 #изменение колличества варнов, аргумент warns - любая цифра

    def set_warn(user_id, warns):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f" UPDATE users SET warns = {warns} WHERE user_id = '{user_id}'")
        conn.commit()

 #изменение времени мута (дата мута меняется)

    def set_mute(user_id, mutes):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f" UPDATE users SET mutes = '{mutes}' WHERE user_id = '{user_id}'")
        conn.commit()

 #изменение привязанных к пользователю ролей (айди привязанных ролей менять)

    def set_role_id(user_id, role_id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f" UPDATE users SET role_id = '{role_id}' WHERE user_id = '{user_id}'")
        conn.commit()

 ############################################################################################################################################################ добавление роли
 #  аргумени id - айди роли (её номер) 
 #  аргумент time_role - время добавления на сервер (формат даты - SS-MM-HH DD-MM-YYYY),
 #  аргумент name сама роль (надпись),
 #  аргумент cost цена роли,
 #  аргумент creator это id_user создателя (айди создателя name роли)

    def add_new_role(id, name, cost, time_role, creator):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"INSERT INTO roles (id, name, cost, time_role, creator) VALUES ('{id}', '{name}', '{cost}', '{time_role}', '{creator}')")
        conn.commit() 

 ############################################################################################################################################################ удаление роли

    def delete_role(id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"DELETE from roles where id = '{id}'")
        conn.commit() 

 ################################################################################################### проверки:

 #проверка name роли (сама надпись роли)

    def role_check_name(id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"SELECT name FROM roles WHERE id = '{id}'")
        return str(curs.fetchone())[1:-2]

 #проверка cost роли (цены роли) 

    def role_check_cost(id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"SELECT cost FROM roles WHERE id = '{id}'")
        return re.sub("[^0-9]", "", str(curs.fetchone()))

 #проверка time_role (времени создания роли)

    def role_check_time(id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"SELECT time_role FROM roles WHERE id = '{id}'")
        return re.findall(r"\d{2}-\d{2}-\d{2} \d{2}-\d{2}-\d{4}", str(curs.fetchone()))

 #проверка creator роли, id_user создателя роли (айдишник создателя роли)

    def role_check_creator(id):
        conn = sqlite3.connect('first_db.db', check_same_thread=False)
        curs = conn.cursor()

        curs.execute(f"SELECT creator FROM roles WHERE id = '{id}'")
        return str(curs.fetchone())[1:2]