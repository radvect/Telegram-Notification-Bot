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
def db_add_parameter_DUD(user_id: int, DUD: int):
	cursor.execute('UPDATE users SET DUD = ? WHERE USER_ID= ?', (DUD, user_id))
	conn.commit()
def db_add_parameter_conditioner(user_id: int, cond: int):
	cursor.execute('UPDATE users SET Cond = ? WHERE USER_ID= ?', (cond, user_id))
	conn.commit()

def db_get_parameter_DUD(user_id: int):
	cursor.execute("SELECT DUD FROM users WHERE USER_ID = ?", (user_id,))
	result = cursor.fetchone()
	if result:
		return result[0]

def db_get_parameter_Cond(user_id: int):
	cursor.execute("SELECT Cond FROM users WHERE USER_ID = ?", (user_id,))
	result = cursor.fetchone()
	if result:
		return result[0]

def get_status(user_id: int):
	cursor.execute("SELECT * FROM users WHERE USER_ID = ?", (user_id,))
	result = cursor.fetchall()
	if result:
		return result[0]