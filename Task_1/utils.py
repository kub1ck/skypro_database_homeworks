import csv


def get_data(file_path: str) -> list:
    """
    Получаем всю информацию из файла в виде списка списков
    """

    with open(file_path, encoding='utf-8') as file:
        return list(csv.reader(file))


def get_unique_names(data: list, index: int) -> dict:
    """
    Получаем словарь, где ключ - имя, значение - индекс
    """

    unique_names: set = set([row[index] for row in data[1:]])

    return {name: index + 1 for index, name in enumerate(unique_names)}


def update_file(names: dict, file_name: str) -> None:
    """
    Записываем csv-файл
    """

    with open('data/' + file_name, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for name, index in names.items():
            writer.writerow([index, name])


def update_main_file(data: list, authors: dict, addresses: dict) -> None:
    """
    Записываем новый ads.csv файл
    """

    with open('data/new_ads.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        for row in data[1:]:
            row[2] = authors[row[2]]
            row[5] = addresses[row[5]]

            writer.writerow(row)
