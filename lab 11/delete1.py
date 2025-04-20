import psycopg2 as pgsql

def create_delete_procedure():
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='D1lnaz_didi',
            host='localhost',
        )
        con = connection.cursor()

        con.execute("""
            CREATE OR REPLACE PROCEDURE delete_by_pattern(pattern TEXT)
            LANGUAGE plpgsql
            AS $$
            BEGIN
                DELETE FROM phonebook
                WHERE name = pattern
                OR surname = pattern
                OR phone = pattern;
            END;
            $$;
        """)

        connection.commit()
        print("Stored procedure 'delete_by_pattern' created successfully.")

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

def delete_data_by_pattern(pattern):
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='D1lnaz_didi',
            host='localhost',
        )
        con = connection.cursor()

        con.callproc('delete_by_pattern', (pattern,))
        
        connection.commit()
        print(f"Deleted records matching '{pattern}'.")

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

if __name__ == "__main__":
    create_delete_procedure()

    pat = input('Who do you want to delete (name/surname/phone)? ')
    delete_data_by_pattern(pat)