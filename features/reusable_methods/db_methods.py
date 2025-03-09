import mysql.connector
# import pyodbc
# Database connection setup
def get_db_connection():
    """Establish and return a MySQL database connection."""
    return mysql.connector.connect(
        host="your_host",
        user="your_user",
        password="your_password",
        database="your_db"
    )

def get_row_count(table_name):
    """Helper function to fetch row count from a table."""
    with mysql.connector.connect(get_db_connection) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            return cursor.fetchone()[0]


def fetch_db_data(conn, query):
    """Fetch data from the database and return results."""
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()