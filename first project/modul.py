import telebot
from telebot import types
token = '5872864892:AAGOrkwB4e1L0rLV4Pm7VH7CkXiBaTetoKw'

bot = telebot.TeleBot(token)




@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
        bot.send_message(message.chat.id, 'Вооу 💣', parse_mode='html')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт', url='https://www.forbes.ru/'))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)

@bot.message_handler(commands=['kanal'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить канал', url='https://t.me/olesyatrader'))
    bot.send_message(message.chat.id, 'Перейдите на канал', reply_markup=markup)

@bot.message_handler(commands=['start'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.InlineKeyboardButton('САЙТ')
    start = types.InlineKeyboardButton('БЕСПЛАТНЫЙ ГАЙД')
    kanal = types.InlineKeyboardButton('КАНАЛ')
    mes = f' Привет , {message.from_user.first_name} {message.from_user.last_name} ✌'
    markup.add(website, start, kanal)
    bot.send_message(message.chat.id, mes, reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'И тебе того же 👋', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'Твой ID:{message.from_user.id}', parse_mode='html')
    elif message.text == 'Фото':
        photo = open('love.jpeg', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == 'БЕСПЛАТНЫЙ ГАЙД':
        document = open('5 ошибок начинающего инвестора.pdf', 'rb').read()
        bot.send_document(message.chat.id, document)
    elif message.text == 'САЙТ':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Посетить сайт', url='https://www.forbes.ru/'))
        bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)
    elif message.text == 'СТАРТ':
        mes = f' Привет , {message.from_user.first_name} {message.from_user.last_name}  ✌'
        bot.send_message(message.chat.id, mes, parse_mode='html')
    elif message.text == 'КАНАЛ':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Посетить канал', url='https://t.me/olesyatrader'))
        bot.send_message(message.chat.id, 'Перейти на канал', reply_markup=markup)


    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю', parse_mode='html')

@bot.message_handler(commands=['start'])
def start_message(message):
    mes = f' Привет , {message.from_user.first_name} {message.from_user.last_name} ✌'
    bot.send_message(message.chat.id, mes, parse_mode='html')


# bot.polling(none_stop=True) - если метод снизу не будет работать
bot.infinity_polling(timeout=10, long_polling_timeout = 5)