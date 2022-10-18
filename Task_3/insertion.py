from psycopg2 import connect
from utils import execute_request


def insert_types(cursor: connect) -> None:
    """
        Заполнение данных в таблице types
    """

    request = """
        INSERT INTO types (name)
            SELECT DISTINCT animal_type FROM old_table
            WHERE animal_type <> ''
    """

    execute_request(cursor, request)


def insert_breeds(cursor: connect) -> None:
    """
        Заполнение данных в таблице breeds
    """

    request = """
        INSERT INTO breeds (name)
            SELECT DISTINCT breed FROM old_table
            WHERE breed <> ''
    """

    execute_request(cursor, request)


def insert_colours(cursor: connect) -> None:
    """
        Заполнение данных в таблице colours
    """

    request = """
        INSERT INTO colours (name)
            SELECT DISTINCT color1 FROM old_table
            WHERE color1 <> ''
    """

    execute_request(cursor, request)


def insert_animals(cursor: connect) -> None:
    """
        Заполнение данных в таблице animals
    """

    request = """
        INSERT INTO animals
            SELECT animal_id, old_table.name, types.id, breeds.id, colour1.id, colour2.id, date_of_birth 
                FROM old_table
                LEFT JOIN types ON old_table.animal_type = types.name
                LEFT JOIN breeds ON old_table.breed = breeds.name
                LEFT JOIN colours as colour1 ON old_table.color1 = colour1.name
                LEFT JOIN colours as colour2 ON old_table.color2 = colour2.name
                GROUP BY animal_id, old_table.name, types.id, breeds.id, colour1.id, colour2.id, date_of_birth 
    """

    execute_request(cursor, request)


def insert_outcome_subtypes(cursor: connect) -> None:
    """
        Заполнение данных в таблице outcome_subtypes
    """

    request = """
        INSERT INTO outcome_subtypes (name)
            SELECT DISTINCT outcome_subtype FROM old_table
            WHERE outcome_subtype <> ''
    """

    execute_request(cursor, request)


def insert_outcome_types(cursor: connect) -> None:
    """
        Заполнение данных в таблице outcome_types
    """

    request = """
        INSERT INTO outcome_types (name)
            SELECT DISTINCT outcome_type FROM old_table
            WHERE outcome_type <> ''
    """

    execute_request(cursor, request)


def insert_shelter(cursor: connect) -> None:
    """
        Заполнение данных в таблице shelter
    """

    request = """
        INSERT INTO shelter
            SELECT index, animal_id, outcome_subtypes.id, outcome_month, outcome_year, outcome_types.id, age_upon_outcome
                FROM old_table
                LEFT JOIN outcome_subtypes ON old_table.outcome_subtype = outcome_subtypes.name
                LEFT JOIN outcome_types ON old_table.outcome_type = outcome_types.name
    """

    execute_request(cursor, request)


def run_insertion_tables(cursor: connect) -> None:
    """
        Запуск процесса заполнения данных во всех таблицах
    """

    insert_types(cursor)
    insert_breeds(cursor)
    insert_colours(cursor)
    insert_animals(cursor)
    insert_outcome_subtypes(cursor)
    insert_outcome_types(cursor)
    insert_shelter(cursor)
