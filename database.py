import sqlite3

conect_database = sqlite3.connect('Banco de dados.db')

cursor = conect_database.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Username TEXT NOT NULL,
               Email  TEXT UNIQUE NOT NULL,
               Password TEXT NOT NULL,
               ConfirPassword TEXT NOT NULL
)
""")

print('conexão ao banco de dados feita com sucesso!')
