<<<<<<< HEAD
# t.me/idfinderusernamebot
=======
>>>>>>> origin/initialisation_of_project
import telebot

bot = telebot.TeleBot('5311521567:AAG9VE60wdLO6RCkyrFJeQmzjf8nZJHrBmE')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Бот на связи. Напиши что-нибудь.')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, f"Ваш ID: {message.from_user.id}")
    bot.send_message(message.chat.id, f"Чат ID: {message.chat.id}")
    bot.send_message(message.chat.id, f"Вы написали: {message.text}")


bot.polling(none_stop=True, interval=0)
