import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

TELEGRAM_TOKEN = '7712072574:AAHI0V1yQMLN9bCkP68QrEE8X4PuotQ4_ss'
API_KEY = '7e3131feef713eb841cc15ea7ac399a6'
CITY = 'Samara'

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


def get_weather(city):
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]

        temp = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']

        return f'Погода в городе {city}:\n' \
               f'Температура: {temp}°C\n' \
               f'Давление: {pressure} гПа\n' \
               f'Влажность: {humidity}%\n' \
               f'Описание: {description.capitalize()}'
    else:
        return 'Город не найден или возникла ошибка!'


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Здравствуйте! Напишите /weather, чтобы узнать погоду в Самаре.')


@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    weather_info = get_weather(CITY)
    await message.answer(weather_info)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)