import telebot
from dotenv import load_dotenv
import os
import requests


load_dotenv()
TOKEN =  os.getenv('botToken')
git_url = os.getenv('gitURL')
bot = telebot.TeleBot(token=TOKEN)

class GetImageAudio():
    api_image = "https://api.thecatapi.com/v1/images/search"

    
    @classmethod
    def get_image(cls):
        return requests.get(cls.api_image).json()[0].get("url")
    
    @classmethod
    def get_audio(cls):
        return requests.get(cls.audio_file)

    

    


@bot.message_handler(commands=["start"])
def greeting(message: telebot.types.Message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.add("get photo", "get audio", "get repo")
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
            photo=GetImageAudio.get_image()
        
        )
    elif message.text == "get audio":
        bot.send_audio(
            chat_id=message.from_user.id, 
            audio="https://github.com/A1kawa1/oop_laba1/blob/main/audio/Ludovico_Einaudi_Fly.mp3"
        )
    elif message.text == "get repo":
        bot.send_message(
            chat_id=message.from_user.id,
            text=git_url
        )

bot.infinity_polling(timeout=600)