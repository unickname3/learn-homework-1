"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def activity_by_age(age):
    if age <= 0:
        return "Некорректное значение возраста."
    elif 0 < age < 7:
        return "Вы посещаете детский сад."
    elif 7 <= age <= 17:
        return "Вы учитесь в школе."
    elif 17 < age <= 22:
        return "Вы учитесь в вузе."
    else:
        return "Вы работаете"


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input("Введите свой возраст: "))
    activity = activity_by_age(age)
    print(activity)


if __name__ == "__main__":
    main()
