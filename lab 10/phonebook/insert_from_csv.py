import psycopg2
import csv
from config import load_config

def insert_from_csv(filename):
    config = load_config()
    with psycopg2.connect(**config) as conn:
        with conn.cursor() as cur:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    cur.execute('INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)', (row[0], row[1], row[2])) 
            print("Data inserted from CSV")

if __name__ == '__main__':
    insert_from_csv("C:\\Users\\zhuma\\OneDrive\\Рабочий стол\\PP2 labs\\lab 10\\phonebook\\data.csv")
