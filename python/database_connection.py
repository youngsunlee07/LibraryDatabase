import psycopg2

def connect_db():
    conn = psycopg2.connect(
        host="localhost",
        database="librarydatabase",
        user="postgres",
        password="1234"
    )
    return conn

def close_db(conn):
    conn.close()