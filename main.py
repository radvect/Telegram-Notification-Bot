import telebot
import database_init
from telebot import types
with open("venv/token.txt","r") as f:
    token = f.readline()

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Shalom! This bot will help you to find the flat of your dream')
	bot.send_message(message.chat.id,'Choose from the /city /space /price /room /dud /conditioner')
	id = message.from_user.id
	print(id)
	database_init.db_init_user(id)


bot.polling()