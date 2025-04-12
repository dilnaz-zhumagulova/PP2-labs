import psycopg2
from config import load_config

def query_data(name_filter=None, surname_filter=None, phone_filter=None):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            if name_filter:
                cur.execute('SELECT * FROM phonebook WHERE name ILIKE %s', (f'%{name_filter}%',))
            elif surname_filter:
                cur.execute('SELECT * FROM phonebook WHERE surname LIKE %s', (f'%{surname_filter}%',))
            elif phone_filter:
                cur.execute('SELECT * FROM phonebook WHERE phone LIKE %s', (f'%{phone_filter}%',))
            else:
                cur.execute('SELECT * FROM phonebook')
            rows = cur.fetchall()
            for row in rows:
                print(row)

if __name__ == '__main__':
    query_data(name_filter='Dil')
