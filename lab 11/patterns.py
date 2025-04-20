import psycopg2 as pgsql

def search_records(pattern):
    connection = None
    con = None
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='D1lnaz_didi',
            host='localhost',
        )
        con = connection.cursor()

        query = """
            SELECT * FROM phonebook
            WHERE name ILIKE %s OR surname ILIKE %s OR phone ILIKE %s
        """
        con.execute(query, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))

        records = con.fetchall()

        return records

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
        return []  # so that code doesn't crash
    finally:
        if con:
            con.close()
        if connection:
            connection.close()

if __name__ == '__main__':
    pattern = input("Search: ... ")
    same_records = search_records(pattern)
    print("Same Records:")
    for record in same_records:
        print(record)
