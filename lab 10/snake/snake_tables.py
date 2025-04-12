from config import load_config  
import psycopg2

config = load_config(filename=r"C:\Users\zhuma\OneDrive\Рабочий стол\PP2 labs\lab 10\snake\snake_database.ini")  
conn = psycopg2.connect(**config)

conn.autocommit = True
cur = conn.cursor()


sql1 = '''
CREATE TABLE IF NOT EXISTS users(
   user_id SERIAL PRIMARY KEY,
   username VARCHAR(255) UNIQUE NOT NULL
);
'''

sql2 = '''
CREATE TABLE IF NOT EXISTS user_score(
   score_id SERIAL PRIMARY KEY,
   user_id INT NOT NULL,
   score INT NOT NULL,
   level INT NOT NULL,
   FOREIGN KEY (user_id) REFERENCES users (user_id)
);
'''

cur.execute(sql1)
cur.execute(sql2)

print("Tables have been created successfully")

cur.close()
conn.close()