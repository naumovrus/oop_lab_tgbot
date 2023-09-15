import telebot
from dotenv import load_dotenv
import os
import requests
import random


load_dotenv()
TOKEN =  os.getenv('botToken')
git_url = os.getenv('gitURL')
bot = telebot.TeleBot(token=TOKEN)
audio_slice = ["https://github.com/naumovrus/oop_lab_tgbot/blob/main/audio/Dior%20(Bonus)%20-%20Pop%20Smoke.m4a", "https://github.com/naumovrus/oop_lab_tgbot/blob/main/audio/LET%20GO%20-%20Central%20Cee.m4a"]

class GetImage():
    api_image = "https://api.thecatapi.com/v1/images/search"

    
    @classmethod
    def get_image(cls):
        return requests.get(cls.api_image).json()[0].get("url")
    


@bot.message_handler(commands=["start"])
def greeting(message: telebot.types.Message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.add("get photo", "get audio", "get repo", "end")
    bot.send_message(
        chat_id=message.from_user.id,
        text="Привет! Я могу высылать изображения, аудио и отправлять ссылку на git.",
        reply_markup=keyboard
    )

@bot.message_handler(content_types=["text"])
def get_media(message: telebot.types.Message):
    if message.text == "get photo":
        bot.send_photo(
            chat_id=message.from_user.id,
            photo=GetImage.get_image()
        
        )
    elif message.text == "get audio":
        bot.send_audio(
            chat_id=message.from_user.id, 
            audio=audio_slice[random.randint(0, 1)]
        )
    elif message.text == "get repo":
        bot.send_message(
            chat_id=message.from_user.id,
            text=git_url
        )

@bot.message_handler(commands=['end'])
def end(message: telebot.types.Message):
    bot.stop_polling


bot.polling(timeout=600)