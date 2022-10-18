from psycopg2 import connect
from utils import execute_request


def create_user_1(cursor: connect) -> None:
    """
    Создаем пользователя user_1 с правами role_one
    """

    request = """
        CREATE USER user_1;
        GRANT role_one TO user_1
    """

    execute_request(cursor, request)


def create_user_2(cursor: connect) -> None:
    """
        Создаем пользователя user_2 с правами role_two
    """

    request = """
        CREATE USER user_2;
        GRANT role_two TO user_2
    """

    execute_request(cursor, request)


def run_creation_users(cursor: connect) -> None:
    """
        Запуск процесса создания пользователей
    """

    create_user_1(cursor)
    create_user_2(cursor)
