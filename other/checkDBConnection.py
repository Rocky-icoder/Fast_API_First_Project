import psycopg2
from psycopg2 import OperationalError

def check_credentials(db_name, user, password):
    try:
        connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host="localhost"
        )
        print("Login successful for user:", user)
    except OperationalError as e:
        print("Login failed:", e)

# Usage
check_credentials("school_db", "postgres", "admin")