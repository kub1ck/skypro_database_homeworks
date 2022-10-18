from utils import *
from creation import *
from insertion import *


def main() -> None:
    connection = db_connect()

    if not connection:
        exit()

    cursor = connection.cursor()

    run_creation_tables(cursor)
    run_insertion_tables(cursor)

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
