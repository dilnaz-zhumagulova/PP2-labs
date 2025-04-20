import psycopg2 as pgsql

def create_many_users_procedure():
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='D1lnaz_didi',
            host='localhost',
        )
        con = connection.cursor()

        con.execute("""
            CREATE OR REPLACE FUNCTION insert_many_users(names TEXT[], surnames TEXT[], phones TEXT[]) RETURNS TEXT[] AS $$
            DECLARE
                invalid_data TEXT[] := ARRAY[]::TEXT[];  -- initialize empty array
                i INT := 1;
            BEGIN
                WHILE i <= array_length(names, 1) LOOP
                    IF phones[i] !~ '^\\d{11}$' THEN  -- checks that phone has exactly 11 digits
                        invalid_data := array_append(invalid_data, names[i] || ' - ' || phones[i]);
                    ELSE
                        INSERT INTO phonebook (name, surname, phone) VALUES (names[i], surnames[i], phones[i]);
                    END IF;
                    i := i + 1;
                END LOOP;
                RETURN invalid_data;
            END;
            $$ LANGUAGE plpgsql;
        """)

        connection.commit()
        print("Stored procedure created successfully!")
    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

def insert_many_users(names, surnames, phones):
    try:
        connection = pgsql.connect(
            database="phonebook",
            user='postgres',
            password='D1lnaz_didi',
            host='localhost',
        )
        con = connection.cursor()

        con.callproc('insert_many_users', (names, surnames, phones))
        invalid_data = con.fetchone()[0]  

        if invalid_data:
            print("Invalid data:")
            for data in invalid_data:
                print(data)
        else:
            print("All users inserted successfully!")

        connection.commit()

    except pgsql.Error as e:
        print("Error while connecting to PostgreSQL", e)
    finally:
        if connection:
            con.close()
            connection.close()

create_many_users_procedure()

names = ['Aizere', 'Arsen', 'Liya']
surnames = ['Saifolla', 'Bekeshov', 'Urangali']
phones = ['87782223344', '5566', '7788']  # 5566 and 7788 will be invalid

insert_many_users(names, surnames, phones)
