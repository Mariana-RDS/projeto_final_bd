import pandas as pd
import sqlite3

# Criar DataFrame de contatos
contatos_data = pd.DataFrame({
    'id_contato': [1, 2, 3, 4],
    'nome': ['Alice', 'Maria', 'Roberto', 'Samanta'],
    'telefone': ['993845678', '972834569', '914327483', '990346785'],
    'email': ['alice@example.com', 'maria@example.com', 'roberto@example.com', 'sam@example.com']
})

# Criar banco de dados e salvar o DataFrame como tabela
conn = sqlite3.connect('agenda.db')

# Usar o método to_sql para salvar o DataFrame como tabela
contatos_data.to_sql('contatos', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()
