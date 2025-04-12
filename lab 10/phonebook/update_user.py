import psycopg2
from config import load_config

def update_user(name, new_name=None, new_surname=None, new_phone=None):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            if new_name:
                cur.execute('UPDATE phonebook SET name = %s WHERE name = %s', (new_name, name))
            if new_surname:
                cur.execute('UPDATE phonebook SET surname = %s WHERE name = %s', (new_surname, name))
            if new_phone:
                cur.execute('UPDATE phonebook SET phone = %s WHERE name = %s', (new_phone, name))
            print("Data updated.")

if __name__ == '__main__':
    update_user('Dilnaz', new_phone='87778889999')
