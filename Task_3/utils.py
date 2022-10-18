from psycopg2 import connect, Error
from typing import Any

from test_settings import *


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

        connection.autocommit = True

        return connection

    except Error as error:
        print('Connection FAILED:', error)

        return False


def execute_request(cursor: connect, request: str) -> None:
    try:
        cursor.execute(request)
    except Error as error:
        print(error)
