from psycopg2 import connect
from utils import execute_request


def create_role_1(cursor: connect) -> None:
    """
        Создаем роль с правами role_one
    """

    request = """
        CREATE ROLE role_one;
        GRANT CONNECT ON DATABASE task_3 TO role_one;
        GRANT SELECT ON ALL TABLES IN SCHEMA public TO role_one; 
    """

    execute_request(cursor, request)


def create_role_2(cursor: connect) -> None:
    """
        Создаем роль с правами role_two
    """

    request = """
        CREATE ROLE role_two;
        GRANT CONNECT ON DATABASE task_3 TO role_two;
        GRANT INSERT ON ALL TABLES IN SCHEMA public TO role_two;
        GRANT UPDATE ON ALL TABLES IN SCHEMA public TO role_two; 
    """

    execute_request(cursor, request)


def run_creation_roles(cursor: connect) -> None:
    """
        Запуск процесса создания ролей
    """

    create_role_1(cursor)
    create_role_2(cursor)
