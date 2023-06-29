import webbrowser

from settings import TOKEN
import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn01 = types.KeyboardButton('Перейти на сайт')
    btn02 = types.KeyboardButton('Удалить фото')
    markup.row(btn01, btn02)
    _file = open('de0476ab09dc099518693b2824cee3d0_xxl.webp', 'rb')
    bot.send_photo(message.chat.id, _file, reply_markup=markup)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} ', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Сайт открыт')
    elif message.text == 'Удалить фотографию':
        bot.send_message(message.chat.id, 'Фото удалено')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Напишите <b>start</b>', parse_mode='html')


@bot.message_handler(commands=['web'])
def web(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть в браузере', url='https://ya.ru'))
    bot.send_message(message.chat.id, 'Откроем сайт...', reply_markup=markup)
    # webbrowser.open('https://ya.ru')


@bot.message_handler()
def text_id_reply(message):
    if 'id' in message.text:
        bot.reply_to(message, f'Ваш id: {message.from_user.id}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn01 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn02 = types.InlineKeyboardButton('Редактировать текст', callback_data='edit')
    markup.row(btn01, btn02)
    bot.reply_to(message, 'Клаccное фото!', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    if callback.data == 'edit':
        bot.edit_message_text(callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)
