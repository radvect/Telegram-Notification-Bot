import telebot
from telebot import types
with open("venv/token.txt","r") as f:
    token = f.readline();

bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Shalom! This bot will help you to find the flat of your dream')


bot.polling()