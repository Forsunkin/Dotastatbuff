from keys import telegram_token as token
import telebot
from telebot import types
from data import turbo_values as turbo_values

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['turbo'])
def start_message(message):
	bot.send_message(message.chat.id, turbo_values)


@bot.message_handler(commands=['button'])
def button_message(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Кнопка")
	markup.add(item1)


bot.infinity_polling()
