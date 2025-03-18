import sqlite3
from db.connection import get_db_connection
from utils.formatters import format_values_to_dump
import sqlite3

def execute_query(query, params=(), fetch_one=False):
    conn = get_db_connection()

    if not conn:
        return None
    
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)

        if query.strip().lower().startswith("select"):
            response = cursor.fetchone() if fetch_one else cursor.fetchall()
            return format_values_to_dump(response)
        else:
            conn.commit()
            return cursor.rowcount
    except sqlite3.connector.Error as error:
        print(error)
        conn.close()
        return None
    finally:
        cursor.close()
        conn.close()