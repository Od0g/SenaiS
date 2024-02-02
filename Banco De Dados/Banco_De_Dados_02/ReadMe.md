Para executar digite no terminal:

$ python3 02_create_schema.py
$ sqlite3 clientes.db '.tables'
$ sqlite3 clientes.db 'PRAGMA table_info(clientes)'

Digitando sqlite3 clientes.db '.tables' você verá que a tabela foi criada.

E o comando sqlite3 clientes.db 'PRAGMA table_info(clientes)' retorna os campos da tabela.

Nota: A única diferença, caso você use Python 2 é no print, onde você deve tirar os parênteses. E no início do arquivo é recomendável que se defina a codificação utf-8, que no caso do Python 3 já é padrão.