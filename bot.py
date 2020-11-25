import telebot
import config
import os
import random

# if local server
# bot = telebot.TeleBot(config.TOKEN)


# if heroku
# when deploying the app run this command:
# heroku config:set TOKEN=YOUR_TOKEN
token = os.environ['TOKEN']
bot = telebot.TeleBot(token)


@bot.message_handler()
def handler(message):
    msg = message.text.lower()

    if config.apologize_request == msg:
        bot.send_message(message.chat.id, "{0}, {1.first_name}".format(
            random.choice(config.apologize_response),
            message.from_user))

    for key, value in config.dictionary.items():
        words = value.split(",")
        for word in words:
            if word in msg:
                sti = open(key, 'rb')
                bot.send_sticker(message.chat.id, sti)


bot.polling(none_stop=True)
