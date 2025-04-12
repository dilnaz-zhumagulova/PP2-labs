import psycopg2
from config import load_config

def delete_user(name=None, surname=None, phone=None):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            if name:
                cur.execute('DELETE FROM phonebook WHERE name = %s', (name,))
            elif surname:
                cur.execute('DELETE FROM phonebook WHERE surname = %s', (surname,))
            elif phone:
                cur.execute('DELETE FROM phonebook WHERE phone = %s', (phone,))
            print("Data deleted.")

if __name__ == '__main__':
    delete_user(name='Aynel')
