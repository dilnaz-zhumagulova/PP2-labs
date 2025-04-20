import psycopg2 as pgsql

def create_procedure():
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='D1lnaz_didi',
            host='localhost',
        )
        con = connection.cursor()

        con.execute("""
            CREATE OR REPLACE FUNCTION update_user(name_param TEXT, surname_param TEXT, phone_param TEXT) 
            RETURNS VOID AS 
            $$
            BEGIN
                IF EXISTS (SELECT 1 FROM phonebook WHERE name = name_param OR surname = surname_param) THEN
                    UPDATE phonebook SET phone = phone_param WHERE name = name_param OR surname = surname_param;
                ELSE
                    INSERT INTO phonebook (name, surname, phone) VALUES (name_param, surname_param, phone_param);
                END IF;
            END;
            $$
            LANGUAGE plpgsql;
        """)
        connection.commit()
        print("Procedure created successfully.")

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

def insert_or_update_user(name, surname, phone):
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='D1lnaz_didi',
            host='localhost',
        )
        con = connection.cursor()

        con.callproc('update_user', (name, surname, phone))

        connection.commit()
        print(f"User {name} {surname} inserted/updated successfully.")

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

if __name__ == '__main__':
    create_procedure()  # Create procedure first (only one time)
    
    insert_or_update_user('Dilnaz', 'Zhumagulova', '87781450431')
    insert_or_update_user('Aynel', 'Koshekova', '87770001122')
