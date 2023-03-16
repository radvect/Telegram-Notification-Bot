import sqlite3

conn = sqlite3.connect('/home/salvador/users', check_same_thread=False)
cursor = conn.cursor()


def db_init_user(user_id: int):
    cursor.execute('INSERT INTO users (USER_ID) VALUES (?)',(user_id,))
    conn.commit()
def db_add_parameter_city(user_id: int, city: str):
	cursor.execute('UPDATE users SET City = ? WHERE USER_ID= ?', (city, user_id))
	conn.commit()
def db_add_parameter_space(user_id: int, space: int):
	cursor.execute('UPDATE users SET Space = ? WHERE USER_ID= ?', (space, user_id))
	conn.commit()
def db_add_parameter_price(user_id: int, price: int):
	cursor.execute('UPDATE users SET Price = ? WHERE USER_ID= ?', (price, user_id))
	conn.commit()
def db_add_parameter_room(user_id: int, room: int):
	cursor.execute('UPDATE users SET Room = ? WHERE USER_ID= ?', (room, user_id))
	conn.commit()
# def db_add_parameter_DUD(user_id: int, user_name: str, user_surname: str, username: str):
# 	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
# 	conn.commit()



def db_add_parameter_cond(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO test (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()