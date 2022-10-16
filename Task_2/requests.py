from psycopg2 import connect


def get_all_ads(cursor: connect) -> list:
    """
        Получаем все объявления
    """

    cursor.execute("""
        SELECT ads.name,
               authors.name,
               ads.price,
               ads.description,
               addresses.address
               
        FROM ads 
        JOIN authors ON ads.author_id = authors.id
        JOIN addresses ON ads.address_id = addresses.id
    """)

    return cursor.fetchall()


def get_author_ads(cursor: connect, author: str) -> list:
    """
        Получаем объявления конкретного автора
    """

    cursor.execute(f"""
            SELECT ads.name,
                   authors.name,
                   ads.price,
                   ads.description,
                   addresses.address

            FROM ads 
            JOIN authors ON ads.author_id = authors.id
            JOIN addresses ON ads.address_id = addresses.id
            WHERE authors.name = '{author}'
        """)

    return cursor.fetchall()


def get_price_ads(cursor: connect, start_price: str, end_price: str) -> list:
    """
        Получаем объявления в диапазоне цен
    """

    cursor.execute(f"""
            SELECT ads.name,
                   authors.name,
                   ads.price,
                   ads.description,
                   addresses.address

            FROM ads 
            JOIN authors ON ads.author_id = authors.id
            JOIN addresses ON ads.address_id = addresses.id
            WHERE ads.price >= {start_price} AND ads.price <= {end_price}
            ORDER BY ads.price
        """)

    return cursor.fetchall()


def get_city_ads(cursor: connect, city: str) -> list:
    """
        Получаем объявления конкретного города
    """

    cursor.execute(f"""
            SELECT ads.name,
                   authors.name,
                   ads.price,
                   ads.description,
                   addresses.address

            FROM ads 
            JOIN authors ON ads.author_id = authors.id
            JOIN addresses ON ads.address_id = addresses.id
            WHERE addresses.address LIKE '{city}%'
        """)

    return cursor.fetchall()


def get_author_and_price_ads(cursor: connect, author: str, price: str) -> list:
    """
        Получаем объявления конкретного пользователя и конкретной цены
    """

    cursor.execute(f"""
            SELECT ads.name,
                   authors.name,
                   ads.price,
                   ads.description,
                   addresses.address

            FROM ads 
            JOIN authors ON ads.author_id = authors.id
            JOIN addresses ON ads.address_id = addresses.id
            WHERE authors.name = '{author}' AND ads.price = {price}
        """)

    return cursor.fetchall()

