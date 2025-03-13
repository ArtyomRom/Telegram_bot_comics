# Телеграм канал для публикации комиксов

Этот проект представляет собой телеграм-бота для публикации комиксов в телеграм группу.

## Технологии
 - Python 3.x
 - aiogram для взаимодействия с Telegram API.


## Функции
  - Отправка комиксов


## Установка
 1. Клонируем репозиторий `https://github.com/ArtyomRom/Telegram_bot_comics.git`
 2. Создайте и активируйте виртуальное окружение:
    ```
    python3 -m venv venv
    source venv/bin/activate  # Для Linux/MacOS
    venv\Scripts\activate     # Для Windows
    ```
 3. Установка зависимостей: `pip install -r requirements.txt`
 4. Настройте Telegram бота:
   - Получите токен для вашего бота в `BotFather`.
   - Убедитесь, что бот имеет права администратора в нужной группе, если вы хотите отправлять уведомления администратору.




## Конфигурации
1. Переменные окружения: В проекте используются следующие переменные:

  - `TG_TOKEN`: Токен для вашего Telegram-бота.
  - `CHAT_ID`: ID группы или канала, куда будут отправляться комиксы.


## Как использовать
 - Запуск бота: `python bot.py`. Один запуск скрипта, одна публикация комикса.