import webbrowser

from settings import TOKEN
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Напишите <b>start</b>', parse_mode='html')


@bot.message_handler(commands=['web'])
def web(message):
    webbrowser.open('https://ya.ru')


@bot.message_handler()
def text_id_reply(message):
    if 'id' in message.text:
        bot.reply_to(message, f'Ваш id: {message.from_user.id}')


bot.polling(none_stop=True)
