import sqlite3
import pandas as pd

# Função para realizar o JOIN entre nomes e emails de bancos de dados diferentes pelo id
def join_nomes_emails_diferentes(database_nome, database_email):
    conn = sqlite3.connect(database_nome)

    # Anexa o banco de dados de emails
    conn.execute(f"ATTACH DATABASE '{database_email}' AS emails")

    query = """
        SELECT nomes.id AS id_nome, nomes.nome, emails.id AS id_email, emails.email
        FROM nomes
        LEFT JOIN emails.emails ON nomes.id = emails.id
    """

    result = pd.read_sql_query(query, conn)

    conn.close()

    return result

# Exemplo de utilização do JOIN entre nomes e emails de bancos de dados diferentes
result_nomes_emails_diferentes = join_nomes_emails_diferentes('agenda_nome.db', 'agenda_email.db')

# Exibir o resultado do JOIN
print("Resultado do JOIN entre nomes e emails de bancos de dados diferentes usando id:")
print(result_nomes_emails_diferentes)


############################################################


# Função para realizar o JOIN entre nomes e telefones de bancos de dados diferentes pelo id
def join_nomes_telefones_diferentes(database_nome, database_telefone):
    conn = sqlite3.connect(database_nome)

    # Anexa o banco de dados de telefones
    conn.execute(f"ATTACH DATABASE '{database_telefone}' AS telefones")

    query = """
        SELECT nomes.id AS id_nome, nomes.nome, telefones.id AS id_telefone, telefones.telefone
        FROM nomes
        LEFT JOIN telefones.telefones ON nomes.id = telefones.id
    """

    result = pd.read_sql_query(query, conn)

    conn.close()

    return result

# Exemplo de utilização do JOIN entre nomes e telefones de bancos de dados diferentes
result_nomes_telefones_diferentes = join_nomes_telefones_diferentes('agenda_nome.db', 'agenda_telefone.db')

# Exibir o resultado do JOIN
print("Resultado do JOIN entre nomes e telefones de bancos de dados diferentes usando id:")
print(result_nomes_telefones_diferentes)
