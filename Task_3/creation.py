from psycopg2 import connect
from utils import execute_request


def create_types(cursor: connect) -> None:
    """
        Создание таблицы types в БД
    """

    request = """
        CREATE TABLE IF NOT EXISTS types (
            id SERIAL PRIMARY KEY,
            name VARCHAR(10) NOT NULL
        )
    """

    execute_request(cursor, request)


def create_breeds(cursor: connect) -> None:
    """
        Создание таблицы breeds в БД
    """

    request = """
        CREATE TABLE IF NOT EXISTS breeds (
            id SERIAL PRIMARY KEY,
            name VARCHAR(40) NOT NULL
        )
    """

    execute_request(cursor, request)


def create_colours(cursor: connect) -> None:
    """
        Создание таблицы colours в БД
    """

    request = """
        CREATE TABLE IF NOT EXISTS colours (
            id SERIAL PRIMARY KEY,
            name VARCHAR(20) NOT NULL
        )
    """

    execute_request(cursor, request)


def create_animals(cursor: connect) -> None:
    """
        Создание таблицы animals в БД
    """

    request = """
        CREATE TABLE IF NOT EXISTS animals (
            id VARCHAR(7) PRIMARY KEY,
            name VARCHAR(20),
            fk_type INTEGER,
            fk_breed INTEGER,
            fk_colour1 INTEGER NOT NULL,
            fk_colour2 INTEGER,
            date_of_birth TIMESTAMP,
            
            FOREIGN KEY (fk_type) REFERENCES types (id),
            FOREIGN KEY (fk_breed) REFERENCES breeds (id),
            FOREIGN KEY (fk_colour1) REFERENCES colours (id),
            FOREIGN KEY (fk_colour2) REFERENCES colours (id)
        )
    """

    execute_request(cursor, request)


def create_outcome_subtypes(cursor: connect) -> None:
    """
        Создание таблицы outcome_subtypes в БД
    """

    request = """
        CREATE TABLE IF NOT EXISTS outcome_subtypes (
            id SERIAL PRIMARY KEY,
            name VARCHAR(20) NOT NULL 
        )
    """

    execute_request(cursor, request)


def create_outcome_types(cursor: connect) -> None:
    """
        Создание таблицы outcome_types в БД
    """

    request = """
        CREATE TABLE IF NOT EXISTS outcome_types (
            id SERIAL PRIMARY KEY,
            name VARCHAR(20) NOT NULL 
        )
    """

    execute_request(cursor, request)


def create_shelter(cursor: connect) -> None:
    """
        Создание таблицы shelter в БД
    """

    request = """
        CREATE TABLE IF NOT EXISTS shelter (
            id INTEGER PRIMARY KEY,
            fk_animal VARCHAR(7) NOT NULL,
            fk_outcome_subtype INTEGER,
            outcome_month INTEGER,
            outcome_year INTEGER,
            fk_outcome_type INTEGER,
            age_upon_outcome VARCHAR(40),
            
            FOREIGN KEY (fk_animal) REFERENCES animals (id),
            FOREIGN KEY (fk_outcome_subtype) REFERENCES outcome_subtypes (id),
            FOREIGN KEY (fk_outcome_type) REFERENCES outcome_types (id)
        )
    """

    execute_request(cursor, request)


def run_creation_tables(cursor: connect) -> None:
    """
        Запуск процесса создания всех таблиц
    """

    create_types(cursor)
    create_breeds(cursor)
    create_colours(cursor)
    create_animals(cursor)
    create_outcome_subtypes(cursor)
    create_outcome_types(cursor)
    create_shelter(cursor)
