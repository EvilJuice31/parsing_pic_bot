import os

import telebot
import time
from reddit import get_pic

token = os.getenv('token')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi')


@bot.message_handler(commands=['r'])
def text(message):
    bot.send_message(message.chat.id, 'How many?')
    bot.register_next_step_handler(message, count)


def count(message):
    try:
        n = int(message.text)
        bot.reply_to(message, 'wait')
        if n > 15:
            n = 15
        while n > 0:
            bot.send_message(message.chat.id, get_pic())
            n -= 1
            time.sleep(5)
        bot.send_message(message.chat.id, "that's all")
    except Exception as e:
        bot.reply_to(message, 'oops')


bot.polling()
