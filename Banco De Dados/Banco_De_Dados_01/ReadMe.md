Banco de Dados na Memória Ram
________Código__________

conn = sqlite3.connect(':memory:')

Banco de Dados no SQLite3
--------Código-----------

conn = sqlite3.connect('clientes.db')

Nomes dos Arquivos 
# connect_db.py
# 01_create_db.py

import sqlite3

conn = sqlite3.connect('clientes.db')
conn.close()

Para rodar este programa no terminal e digite:
$ python3 01_create_db.py
$ ls *.db

'''
#Criando uma tabela
'''
Para criar uma tabela no banco de dados usamos dois métodos fundamentais:

cursor: é um interador que permite navegar e manipular os registros do bd.

execute: lê e executa comandos SQL puro diretamente no bd.