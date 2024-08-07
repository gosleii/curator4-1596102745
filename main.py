import telebot

bot = telebot.TeleBot('7487297755:AAES1rEe3lGcPrAro8r0x5quY-vFomvpMhE')


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, какой товар вас интересует?', parse_mode='Markdown')


@bot.message_handler(commands=['new'])
def new_handler(message):
    bot.send_message(message.chat.id, 'В наличии имеется платье розового цвета', parse_mode='Markdown')


@bot.message_handler(commands=['new1'])
def new1_handler(message):
    bot.send_message(message.chat.id, 'Выбрать розовое', parse_mode='Markdown')


@bot.message_handler(commands=['new12'])
def new12_handler(message):
    bot.send_message(message.chat.id, 'Розовое платье стоит 3000 рублей. Вас устраивает цена?', parse_mode='Markdown')


@bot.message_handler(commands=['new123'])
def new123_handler(message):
    bot.send_message(message.chat.id, 'Оформить заказ', parse_mode='Markdown')


bot.infinity_polling()