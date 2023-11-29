import telebot

bot = telebot.TeleBot('6509293174:AAG1ZiKSBW9yo9a4pPJ4ybWMrX86eOfB7Q8')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,
                     '*Здравствуйте, я ваш бот-помощник.* Доступные следующие команды: /hello, /work, /sport, /sleep',
                     parse_mode='Markdown')


@bot.message_handler(commands=['hello'])
def main(message):
    bot.send_message(message.chat.id, '*Привет, привет еще раз, я рад, ято ты используешь мли возможности!!!*',
                     parse_mode='Markdown')


@bot.message_handler(commands=['work'])
def main(message):
    bot.send_message(message.chat.id, 'Чтобы развиваться и двигаться вперед,\nнужно работать над собой!!!',
                     parse_mode='Markdown')


@bot.message_handler(commands=['sport'])
def main(message):
    bot.send_message(message.chat.id,
                     'Вы выбрали команду спорт. Расскажем вам о истории становления спорта. [Ссылка на ресурс] (https://tltolimp.ru/public/?id=20150129-1)',
                     parse_mode='Markdown')


@bot.message_handler(commands=['sleep'])
def main(message):
    bot.send_message(message.chat.id, 'Ты классно поработал сегодня и модешь собой гордиться\nдавай отдыхать!',
                     parse_mode='Markdown')


bot.infinity_polling()