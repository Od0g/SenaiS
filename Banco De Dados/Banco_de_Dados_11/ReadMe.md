Fazendo backup do banco de dados (exportando dados)
Talvez seja este o item mais importante: backup. Observe o uso da biblioteca io que salva os dados num arquivo externo através do método write, e o método iterdump() que exporta a estrutura e dados da tabela para o arquivo externo.

Para executar digite no terminal:

$ python3 11_backup.py
$ cat clientes_dump.sql