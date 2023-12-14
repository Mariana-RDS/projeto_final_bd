import sqlite3
import pandas as pd


def get_table(database_name, table_name):
    conn = sqlite3.connect(database_name)
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df