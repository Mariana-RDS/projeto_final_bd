import sqlite3

#######################################################
    
def create_nomes_table(database_name: str):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nomes (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)

    conn.close()

#####################################################
    
def create_telefones_table(database_name: str):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telefones (
            id INTEGER PRIMARY KEY,
            telefone TEXT NOT NULL
        )
    """)

    conn.close()

#####################################################
    
def create_emails_table(database_name: str):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emails (
            id INTEGER PRIMARY KEY,
            email TEXT NOT NULL
        )
    """)

    conn.close()
