import os
from os import environ
import telebot
API_KEY = environ['API_KEY']
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['greet'])
def greet(message):
  bot.reply_to(message,"wow it worked")

bot.polling()