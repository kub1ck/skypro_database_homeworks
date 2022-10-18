from utils import db_connect
from creation import run_creation_tables
from insertion import run_insertion_tables
from roles import run_creation_roles
from users import run_creation_users


def main() -> None:
    connection = db_connect()

    if not connection:
        exit()

    cursor = connection.cursor()

    run_creation_tables(cursor)
    run_insertion_tables(cursor)

    run_creation_roles(cursor)
    run_creation_users(cursor)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
