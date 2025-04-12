import psycopg2
from config import load_config

def insert_from_console():
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            while True:
                name = input("Enter name (or 'stop'): ")
                if name.lower() == 'stop':
                    break
                surname = input("Enter surname: ")
                phone = input("Enter phone: ")
                cur.execute('INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)', (name, surname, phone))
            print("Data inserted from console.")

if __name__ == '__main__':
    insert_from_console()
