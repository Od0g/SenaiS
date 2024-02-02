Recuperando o banco de dados (importando dados)
Criaremos um novo banco de dados e iremos reconstruir a tabela e os dados com o arquivo clientes_dump.sql. O método read() lê o conteúdo do arquivo clientes_dump.sql e o método executescript() executa as instruções SQL escritas neste arquivo.

Para executar digite no terminal:

$ python3 12_read_sql.py
Banco de dados recuperado com sucesso.
Salvo como clientes_recuperado.db
$ sqlite3 clientes_recuperado.db 'SELECT * FROM clientes;'