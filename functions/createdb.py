import sqlite3

# Criação do banco de dados
def create_db(database_name: str):
    sqlite3.connect('agenda.db')