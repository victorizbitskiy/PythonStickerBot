import telebot
import config
import os

# if local server
# bot = telebot.TeleBot(config.TOKEN)

# if heroku
# when deploying the app run this command:
# heroku config:set TOKEN=YOUR_TOKEN
token = os.environ['TOKEN']
bot = telebot.TeleBot(token)

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