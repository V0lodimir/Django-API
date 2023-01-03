import telebot
from telebot import types
import requests
from db_worker import add_user, message_history
import datetime


bot = telebot.TeleBot('')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Hello")
    btn2 = types.KeyboardButton("Button")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Hello", reply_markup=markup)
    add_user(chat_id=message.chat.id, 
             full_name=str(message.from_user.first_name) + " " + str(message.from_user.last_name), 
             username=str(message.from_user.username), 
             language_code=str(message.from_user.language_code), 
             reg_date=datetime.datetime.now())

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == 'Hello'):
        bot.send_message(message.chat.id, text="Hello, " + message.from_user.first_name)
    elif(message.text == 'Button'):
        bot.send_message(message.chat.id, text="Hello, " + message.from_user.last_name)
    elif(message.text == '/mem'):
        member = []
        member = bot.get_chat_member(chat_id='1001509118604', user_id=message.from_user.id)
    elif(message.text == '/bin'):
        bot.send_message(message.chat.id, user_id=message.from_user.id, until_date=40)
        bot.send_message(message.chat.id, text="Ban")
    '''else:
        bot.send_message(message.chat.id, text="Comand not found")
        '''
    message_history(message_id = message.message_id,
                    chat_id = message.chat.id,
                    full_name = str(message.from_user.first_name) + " " + str(message.from_user.last_name),
                    username = str(message.from_user.username),
                    date = datetime.datetime.now(),
                    text = message.text)


bot.polling(none_stop=True, interval=0)
