import telebot;
bot = telebot.TeleBot('1929269998:AAFqlLEJ0jnMVcwg5FziWHyR3budKvdC1PE');


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "хуй":
        bot.send_message(message.from_user.id, "")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Хуй")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)
