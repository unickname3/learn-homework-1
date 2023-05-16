"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def strings_compare(s1, s2):
    if type(s1) != str or type(s2) != str:
        return 0
    if s1 == s2:
        return 1
    if len(s1) > len(s2):
        return 2
    if s2 == "learn":
        return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print('strings_compare(2, "learn") -> ', strings_compare(2, "learn"))
    print('strings_compare("word", "word") -> ', strings_compare("word", "word"))
    print('strings_compare("words", "word") -> ', strings_compare("words", "word"))
    print('strings_compare("word", "learn") -> ', strings_compare("word", "learn"))
    print('strings_compare("word", "words") -> ', strings_compare("word", "words"))


if __name__ == "__main__":
    main()
