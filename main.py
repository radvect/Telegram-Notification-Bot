import telebot
import database_init
from telebot import types
with open("venv/token.txt","r") as f:
    token = f.readline()

bot=telebot.TeleBot(token)

cities = ["/Tel_Aviv", "/Rishon", "/Holon", "/Haifa", "/Ramat_Gan", "/Eilat"]
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Shalom! This bot will help you to find the flat of your dream')
	bot.send_message(message.chat.id,'Choose from the /city /space /price /room /dud /conditioner')
	id = message.from_user.id
	print(id)
	database_init.db_init_user(id)
@bot.message_handler(commands=['city'])
def city_message(message):

	bot.send_message(message.chat.id,'Сhoose a city')
	msg = bot.send_message(message.chat.id,' '.join(cities))

	bot.register_next_step_handler(msg, city)


def city(message):
	break_cond = cities.count(message.text)
	if(break_cond==0):
		msg  = bot.send_message(message.chat.id,"Search in this city is unable, choose another")
		bot.register_next_step_handler(msg, city)
	else:
		database_init.db_add_parameter_city(message.from_user.id, str(message.text[1:]))


bot.polling()