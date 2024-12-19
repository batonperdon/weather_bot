Импорт библиотек

import logging
import requests
from aiogram import Bot, Dispatcher, executor, types


 logging: Библиотека для ведения логов. В данном коде не используется, но обычно она помогает отслеживать события и ошибки в приложении.

 requests: Библиотека для выполнения HTTP-запросов. Здесь она используется для обращения к API погоды.

 aiogram: Библиотека для работы с Telegram Bot API. Она предоставляет инструменты для создания ботов и обработки команд и сообщений.

Константы

TELEGRAM_TOKEN = 'ваш_токен'
API_KEY = 'ваш_ключ_API'
CITY = 'Samara'


 TELEGRAM_TOKEN: Токен вашего Telegram-бота, полученный от BotFather. Он используется для аутентификации бота в Telegram.

 API_KEY: Ключ API для доступа к OpenWeatherMap. Он необходим для выполнения запросов к этому сервису.

 CITY: Название города, для которого будет запрашиваться информация о погоде (в данном случае "Самара").

Инициализация бота

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)


 bot: Создается экземпляр бота с использованием токена. Этот объект будет использоваться для отправки сообщений и взаимодействия с пользователями.

dp: Создается диспетчер (Dispatcher), который отвечает за обработку входящих сообщений и команд.

Функция получения погоды

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

        return f'Погода в городе {city}:\n' 
               f'Температура: {temp}°C\n' 
               f'Давление: {pressure} гПа\n' 
               f'Влажность: {humidity}%\n' 
               f'Описание: {description.capitalize()}'
    else:
        return 'Город не найден или возникла ошибка!'


 get_weather(city): Функция, которая принимает название города и делает запрос к API OpenWeatherMap.

   URL: Формируется URL для запроса с параметрами (город, API ключ, единицы измерения и язык).

   response: Выполняется GET-запрос к указанному URL.

   Проверка response.status_code == 200: Если запрос успешен (код 200), данные из ответа преобразуются в JSON.

   Извлечение данных: Извлекаются температура, давление, влажность и описание погоды.

   Возврат информации: Формируется строка с информацией о погоде и возвращается. Если город не найден или произошла ошибка, возвращается сообщение об этом.

Обработчики команд

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Здравствуйте! Напишите /weather, чтобы узнать погоду в Самаре.')


 @dp.message_handler(commands=['start']): Декоратор, который указывает, что эта функция будет обрабатывать команду /start.

 start_command(message): Функция, которая вызывается при получении команды /start. Она отправляет приветственное сообщение пользователю.

@dp.message_handler(commands=['weather'])
async def weather_command(message: types.Message):
    weather_info = get_weather(CITY)
    await message.answer(weather_info)


 @dp.message_handler(commands=['weather']): Декоратор для обработки команды /weather.

 weather_command(message): Функция, которая вызывается при получении команды /weather. Она вызывает функцию get_weather(CITY) для получения информации о погоде в Самаре и отправляет эту информацию пользователю.

Запуск бота

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':: Проверка, запущен ли скрипт напрямую.

