"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data = [
        {
            "product": "iPhone 12",
            "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
        },
        {
            "product": "Xiaomi Mi11",
            "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
        },
        {
            "product": "Samsung Galaxy 21",
            "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
        },
    ]

    total_sold = 0

    for phone in data:
        phone_name = phone["product"]
        total_phone_sold = sum(phone["items_sold"])

        avg_phone_sold = total_phone_sold / len(phone["items_sold"])
        total_sold += total_phone_sold

        print(f"{phone_name} всего продано {total_sold} шт.")
        print(f"Среднее количество продаж {phone_name}: {avg_phone_sold}")

    print(f"Суммарное количество продаж всех товаров: {total_sold}")

    avg_sold_per_phone = total_sold / len(data)
    print(f"Среднее количество продаж всех товаров: {avg_sold_per_phone}")


if __name__ == "__main__":
    main()
