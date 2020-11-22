import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler()
def sap(message):

	if 'sap' in message.text or 'сап' in message.text:
	  sti = open('static/sap_is_shit.webp', 'rb')
	  bot.send_sticker(message.chat.id, sti)

	elif 'abap' in message.text or 'абап' in message.text:
	  sti = open('static/abap_is_shit.webp', 'rb')
	  bot.send_sticker(message.chat.id, sti)

	elif 'python' in message.text or 'питон' in message.text:
	    sti = open('static/python_is_perfectly.png', 'rb')
	    bot.send_sticker(message.chat.id, sti)

bot.polling(none_stop=True)