import psycopg2
import config

def db_connect():
    try:
        conn=psycopg2.connect(
            host=config.host,
            dbname=config.database,
            user=config.user,
            password=config.password
        )
        return conn
    except Exception as e:
        print("Connection error:", e)
        return None
