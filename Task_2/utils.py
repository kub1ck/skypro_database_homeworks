from requests import *
from test_settings import *

from psycopg2 import connect, Error
from typing import Any


def db_connect() -> Any:
    """
        Подключение к бд
    """

    try:
        connection = connect(
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            host=HOST,
            port=PORT
        )

        return connection

    except Error as error:
        print('Connection FAILED:', error)

        return False


def get_alpha() -> str:
    """
        Возвращаем текст, содержащий только буквы
    """

    while True:
        user_input = input("Ввод: ")

        if user_input.isalpha() and ' ' not in user_input:
            return user_input

        print("\nНужно ввести текст, содержащий только буквы!")


def get_data(cursor: connect, request_number: str) -> Any:
    """
        Получаем необходимые данные
    """

    match request_number:
        case '0':
            return True

        case '1':
            return get_all_ads(cursor)

        case '2':
            print("\nВведите имя автора")
            author = get_alpha()

            return get_author_ads(cursor, author)

        case '3':
            print("\nВведите нижний предел цены")
            start_price = get_digit()

            print("\nВведите верхний предел цены")
            end_price = get_digit()

            return get_price_ads(cursor, start_price, end_price)

        case '4':
            print("\nВведите город")
            city = get_alpha()

            return get_city_ads(cursor, city)

        case '5':
            print("\nВведите имя автора")
            author = get_alpha()

            print("\nВведите цену")
            price = get_digit()

            return get_author_and_price_ads(cursor, author, price)

        case _:
            print("\nДанный выбор отсутствует.")
            return False


def get_digit() -> str:
    """
        Возвращаем цифры
    """

    while True:
        user_input = input("Ввод: ")

        if user_input.isdigit() and ' ' not in user_input:
            return user_input

        print("\nНужно ввести цифру!")


def show_data(data: list) -> None:
    """
        Вывод объявлений в консоли
    """

    for row in data:
        description = row[3].replace('\n', ' ') if row[3] else ''

        print(f"\nНазвание: {row[0].strip()}",
              f"Автор: {row[1].strip()}",
              f"Цена: {row[2]} руб.",
              f"Описание: {description}",
              f"Адрес: {row[4].strip()}",
              sep='\n')

    input("\nДля продолжения нажмите Enter...")


def show_menu() -> None:
    """
        Выводим меню для пользователя
    """

    print(
        """
        1 - Вывести все объявления.
        2 - Вывести объявления конкретного автора.
        3 - Вывести объявления по диапазону цен.
        4 - Вывести объявления для конкретного города.
        5 - Вывести объявления для конкретного автора и цены.
        
        0 - Выход из программы.
        """
    )
