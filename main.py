from aiogram import *
from config import *
from pytube import YouTube

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_messsage(message:types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Привет! Я могу скачивать видео с Youtube\n"
                           "Отправь мне ссылку")


@dp.message_handler()
async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'http://youtu.be' or 'http://www.youtube.com':
        await bot.send_message(chat_id, f"*Начинаю загрузку видео* : *{yt.title}*\n"
                                        f"* С канала *: [{yt.author}]({yt.channel_url})", parse_mode="Markdown")







if __name__ == '__main__':
    executor.start_polling(dp)