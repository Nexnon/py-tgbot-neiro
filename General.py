import telebot
import time
from PIL import Image, ImageDraw
from Neiro import Calc_rezult
import requests
import os

TOKEN = '1487519075:AAFhoZ1N3Nvd-OcQJfPA6nux80949uyxkn0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет! Это бот способный распознавать, что за цифра на изображении! Отправь мне картинку, а я скажу, что на ней вижу😉')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, 'Это бот способный распознавать, что за цифра на изображении! Отправь мне картинку, а я скажу, что на ней вижу. Чтобы ознакомится с форматом изображения используй команду /format')

@bot.message_handler(commands=['format'])
def format_message(message):
    bot.send_message(message.chat.id, 'Изображение должно быть черно-белым, размером 28x28 пикселей')


@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text != '/help':
        bot.send_message(message.chat.id, 'Я не понимаю тебя, напиши /help, чтобы узнать, что я умею')

@bot.message_handler(content_types=['photo'])
def photo_message(message):
    current_path = os.getcwd()
    num = 0
    file_id_info = bot.get_file(message.photo[0].file_id)
    downloaded_file = bot.download_file(file_id_info.file_path)
    with open(current_path + "/" + 'file.png', 'wb') as new_file:
        new_file.write(downloaded_file)

    image = Image.open(current_path + "/" + 'file.png')
    (width, height) = image.size
    if width == 28 and height == 28:
        num = Calc_rezult(image)
        bot.send_message(message.chat.id, f'Я думаю это цифра {num}') 
    else:
        bot.send_message(message.chat.id, 'Изображение не того формата :( Подробнее о формате можешь узнать вписав команду /format')
    

bot.polling(none_stop=True, interval=0)