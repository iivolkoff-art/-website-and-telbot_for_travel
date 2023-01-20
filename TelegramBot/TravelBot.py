from aiogram import Bot, Dispatcher, executor, types
from TelegramBot.DataBase import DataBase
import logging
from TelegramBot.JSON import JSON
from datetime import datetime
import asyncio


class TravelBot:
    def __init__(self):
        self.TOKEN = '#'
        self.db = DataBase()
        self.json = JSON()

        logging.basicConfig(level=logging.INFO)

        self.bot = Bot(token=self.TOKEN)
        self.dp = Dispatcher(self.bot)

    def start(self):
        @self.dp.message_handler(commands=['start'])
        async def process_start_command(message: types.Message):
            await message.reply("Привет! Бот будет сообщать тебе о новых клиентах, как только они появятся! \nВерсия бота 0.9.2 \n Для проверки новых клиентов введите /check")

    def get_inf(self):
        @self.dp.message_handler(commands=['check'])
        async def echo(message: types.Message):
            # await message.answer(self.db.get_data())
            # await message.answer(self.json.get_last_id())
            await message.answer(self.db.get_data_from_last_id_to_max_id(self.json.get_last_id()))


    def run(self):
        self.start()
        self.get_inf()
        executor.start_polling(self.dp, skip_updates=True)



