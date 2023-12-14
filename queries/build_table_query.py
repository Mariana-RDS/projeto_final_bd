# Construção da query para obter uma tabela
def build_table_query(table_name: str) -> str:
    """Constrói a consulta para recuperar os dados de uma tabela

    Args:
        table_name (str): Nome da tabela

    Returns:
        str: Consulta SQL para obter os dados da tabela
    """
    query = f"""
        SELECT * 
        FROM {table_name}
    """
    return query
