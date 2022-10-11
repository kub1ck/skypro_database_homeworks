from utils import *


def main() -> None:
    file_path = 'ads.csv'
    data = get_data(file_path)

    # Работа с авторами
    authors = get_unique_names(data, 2)

    file_name = 'authors.csv'
    update_file(authors, file_name)

    # Работа с адресами
    addresses = get_unique_names(data, 5)

    file_name = 'addresses.csv'
    update_file(addresses, file_name)

    # Работа с мейн-файлом
    update_main_file(data, authors, addresses)


if __name__ == '__main__':
    main()
