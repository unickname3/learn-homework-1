"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
from datetime import date

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import local_settings

logging.basicConfig(
    format="%(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="bot.log",
)


def greet_user(update, context):
    text = "Вызван /start"
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)


def planet_where(update, context):
    user_text = update.message.text
    try:
        planet = user_text.split()[1].capitalize()
    except IndexError:
        reply = "Введите название планеты"
        update.message.reply_text(reply)
        return

    planet_obj = None
    if planet == "Mercury":
        planet_obj = ephem.Mercury()
    elif planet == "Venus":
        planet_obj = ephem.Venus()
    elif planet == "Mars":
        planet_obj = ephem.Mars()
    elif planet == "Jupiter":
        planet_obj = ephem.Jupiter()
    elif planet == "Saturn":
        planet_obj = ephem.Saturn()
    elif planet == "Uranus":
        planet_obj = ephem.Uranus()
    elif planet == "Neptune":
        planet_obj = ephem.Neptune()

    if planet_obj:
        planet_obj.compute(date.today())
        planets_constellation = ephem.constellation(planet_obj)
        reply = f"{planet} в созвездии {planets_constellation[1]}"
    else:
        reply = "Не знаю планеты такой"

    update.message.reply_text(reply)


def main():
    mybot = Updater(local_settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_where))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
