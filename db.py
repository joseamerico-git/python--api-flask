import mysql.connector

try:
    # Configuração da conexão
    conexao = mysql.connector.connect(
        host="localhost",       # Endereço do servidor MySQL
        user="root",     # Usuário do banco de dados
        password="root",   # Senha do banco de dados
        database="hidrobike3" # Nome do banco de dados
    )

    if conexao.is_connected():
        print("Conexão bem-sucedida!")
        # Criação de um cursor para executar comandos SQL
        cursor = conexao.cursor()
        cursor.execute("SELECT DATABASE();")
        banco = cursor.fetchone()
        print(f"Banco de dados conectado: {banco[0]}")

except mysql.connector.Error as erro:
    print(f"Erro ao conectar: {erro}")

finally:
    # Fechar a conexão
    if 'conexao' in locals() and conexao.is_connected():
        conexao.close()
        print("Conexão encerrada.")
