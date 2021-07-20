import sqlite3
import random
import telebot
from telebot import types
from telebot.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, \
    InlineKeyboardButton

bot = telebot.TeleBot('1858056181:AAG_qGWxjlIt48aah5F8wTpH-uVTJKrdUCo')

conn = sqlite3.connect('Det_Book.db')
cur = conn.cursor()


cur.execute("SELECT * FROM book_collection_new;")
book_lst = cur.fetchall()
print(type(random.choice(book_lst)))
print(random.choice(book_lst))
print('----')
print(book_lst[1])

print('*********')


cur.execute("SELECT * FROM puaro_new;")
puaro_lst = cur.fetchall()
print(type(random.choice(puaro_lst)))
print(random.choice(puaro_lst))
print('----')
print(random.choice(puaro_lst)[1], random.choice(puaro_lst)[2], random.choice(puaro_lst)[3])
print(puaro_lst[1])

print('******')

cur.execute("SELECT * FROM miss_new;")
miss_lst = cur.fetchall()
print(type(random.choice(miss_lst)))
print(random.choice(miss_lst))
print('----')
print(random.choice(miss_lst)[1], random.choice(miss_lst)[2], random.choice(miss_lst)[3])
print(miss_lst[1])


cur.execute("SELECT * FROM battle_new;")
battle_lst = cur.fetchall()
print(type(random.choice(battle_lst)))
print(random.choice(battle_lst))
print('----')
print(random.choice(battle_lst)[1], random.choice(battle_lst)[2], random.choice(battle_lst)[3])
print(battle_lst[1])




@bot.message_handler(commands=['start'])
def start_messages(message):

    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    markup.add(KeyboardButton('Случайный выбор 📖'))

    markup.add(KeyboardButton('Эркюль Пуаро 🔍'),
               KeyboardButton('Мисс Марпл 🔍'),
               KeyboardButton('Инспектор Баттл 🔍'))

    bot.send_message(message.chat.id, 'Привет, я готов порекомендовать тебе захватывающие детективы  Агаты Кристи. Нажми на одну из кнопок', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Случайный выбор 📖":
        cicle_b = random.choice(book_lst)

        bot.send_photo(message.from_user.id, cicle_b[3], caption=cicle_b[1])
        bot.send_message(message.from_user.id, cicle_b[2])


    elif message.text == "Эркюль Пуаро 🔍":
        cicle_p = random.choice(puaro_lst)
        bot.send_photo(message.from_user.id, cicle_p[3], caption=cicle_p[1])
        bot.send_message(message.from_user.id, cicle_p[2])

    elif message.text == "Мисс Марпл 🔍":
         cicle_m = random.choice(miss_lst)
         bot.send_photo(message.from_user.id, cicle_m[3], caption=cicle_m[1])
         bot.send_message(message.from_user.id, cicle_m[2])

    elif message.text == "Инспектор Баттл 🔍":
         cicle_ins = random.choice(battle_lst)
         bot.send_photo(message.from_user.id, cicle_ins[3], caption=cicle_ins[1])
         bot.send_message(message.from_user.id, cicle_ins[2])

    elif message.text.lower() == "марго, ссылка":
        margo = 'Выполняю, ' + message.from_user.first_name
        bot.send_message(message.from_user.id, margo)
        bot.send_message(message.from_user.id,
                         "https://archiveofourown.org/works/25270294?view_adult=true&view_full_work=true")
        bot.send_photo(message.from_user.id,
                       'https://sun9-10.userapi.com/impg/ixqGB7pY97ckvfLXa__D9S4NDJyKp65MLHk35g/smWRh4ssY0E.jpg?size=1200x503&quality=96&sign=2a262448d84421a78c35febf43a90a21&type=album')




    else:
        bot.send_message(message.from_user.id, "Не понимаю")


@bot.message_handler(commands=['margo'])
def margo_mess(mess):
    margo = 'Выполняю, ' + mess.from_user.first_name
    bot.send_message(mess.from_user.id, margo)
    bot.send_message(mess.from_user.id,
                     "https://archiveofourown.org/works/25270294?view_adult=true&view_full_work=true")
    bot.send_photo(mess.from_user.id,
                   'https://sun9-10.userapi.com/impg/ixqGB7pY97ckvfLXa__D9S4NDJyKp65MLHk35g/smWRh4ssY0E.jpg?size=1200x503&quality=96&sign=2a262448d84421a78c35febf43a90a21&type=album')


bot.polling()
