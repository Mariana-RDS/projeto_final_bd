import sqlite3


#########################################################

def add_nome(database_name: str, nome: str):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO nomes (nome) VALUES (?)
    """, (nome,))

    conn.commit()
    conn.close()

#######################################################
    
def add_telefone(database_name: str, telefone: str):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO telefones (telefone) VALUES (?)
    """, (telefone,))

    conn.commit()
    conn.close()

##########################################################
    
def add_email(database_name: str, email: str):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO emails (email) VALUES (?)
    """, (email,))

    conn.commit()
    conn.close()
