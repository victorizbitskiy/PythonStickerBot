import telebot
import config
import os

# bot = telebot.TeleBot(config.TOKEN) # if local server
token = os.environ['TOKEN'] # if heroku

@bot.message_handler()
def sap(message):

	if 'sap' in message.text or 'сап' in message.text:
	  sti = open('static/sap.webp', 'rb')
	  bot.send_sticker(message.chat.id, sti)

	elif 'abap' in message.text or 'абап' in message.text:
	  sti = open('static/abap.webp', 'rb')
	  bot.send_sticker(message.chat.id, sti)

	elif 'python' in message.text or 'питон' in message.text:
	    sti = open('static/python.png', 'rb')
	    bot.send_sticker(message.chat.id, sti)

bot.polling(none_stop=True)