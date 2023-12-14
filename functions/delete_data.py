import sqlite3

#############################################

def delete_nome(database_name: str, nome_id: int):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM nomes WHERE id = ?
    """, (nome_id,))

    conn.commit()
    conn.close()

######################################################
    
def delete_telefone(database_name: str, telefone_id: int):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM telefones WHERE id = ?
    """, (telefone_id,))

    conn.commit()
    conn.close()

##############################################################
    
def delete_email(database_name: str, email_id: int):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM emails WHERE id = ?
    """, (email_id,))

    conn.commit()
    conn.close()
