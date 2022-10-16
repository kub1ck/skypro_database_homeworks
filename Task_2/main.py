from utils import db_connect, get_digit, get_data, show_menu, show_data


def main() -> None:
    connection = db_connect()

    if not connection:
        exit()

    cursor = connection.cursor()

    while True:
        show_menu()

        request_number = get_digit()
        data = get_data(cursor, request_number)

        # Если пользователь ввел '0'
        if data is True:
            break

        # Если вариант отсутствует
        if data is False:
            continue

        if not data:
            print("\nПо вашему запросу ничего не найдено.")
            continue

        show_data(data)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
