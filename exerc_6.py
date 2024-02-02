# 1- O Individuo digita seu nome 
nome = input("Digite seu nome: ")
# 2 - Digita sua Idade
idade = int(input("Digite sua idade: "))
# 3 - Digita seu gênero escolhendo entre a opção "1" e "2". 
genero = int(input("""Seu gênero:
[1] Homem
[2] Mulher
""" ))
''' 3.1 -O usuario digita um das opções 
o código lê o numero caso o numero digitado
seje diferente dos determinados
ele retorna e  pede para o usuario
escolher uma das opções determinadas
 '''
if genero != 1 and genero !=2:
    genero = int(input("""Seu gênero:
[1] Homem
[2] Mulher
""" ))
""" 4 - O usuario digita um das opções 
o código lê o numero caso o numero digitado
seje diferente dos determinados
ele retorna e  pede para o usuario
escolher uma das opções determinadas
"""  

option = int(input("""Validação da aposentadoria por:
[1]idade                         
[2]Tempo de Contribuição
"""))
if option != 1 and option != 2:
    option = int(input("""Validação da aposentadoria por:
[1]idade                         
[2]Tempo de Contribuição
"""))
"""# 5 - O usuario ecolher a opção "1",
 o código irá verificar a aposentadoria pela
 idade.
"""
if option == 1:
    # Se o gênero definido for Homem o código atribuira o valor 1 
    if genero == 1:
        '''Se o gênero definido for Homem o código atribuira o valor 1,
        e verifica se o valor atribuido é realmente 1.'''
        if idade >=63:
            # verifica a idade, se for maior ou igual a 63 é validada.
            print(f"Senhor {nome} sua aposentadoria foi validada.")
        if idade <63:
            # verifica a idade, se for menor a 63 é invalidada.
            print(f"Senhor {nome} sua aposentadoria não foi validada.")
if option == 1:
     # Se o gênero definido for Mulher o código atribuira o valor 2.
    if genero == 2:
        '''Se o gênero definido for Mulher o código atribuira o valor 2,
        e verifica se o valor atribuido é realmente 2.'''
        if idade >=58:
            # verifica a idade, se for maior ou igual a 58 é validada.
            print(f"Senhora {nome} sua aposentadoria foi validada.")
        if idade <58:
            # verifica a idade, se for menor a 58 é invalidada.
            print(f"Senhora {nome} sua aposentadoria não foi validada.")
"""# 6 - Se O usuario ecolher a opção "2",
 o código irá verificar a aposentadoria pelo
 tempo de contribuição."""
if option ==2:
    # Nesta etapa o Código pede para o usuario inserir o tempo contribido.
    tmp_contribuicao=int(input("Digite o tempo de contribuição: "))
    if genero ==2:
        '''Se o gênero definido for Mulher 
        o código verifica se o valor atribuido é realmente 2.'''
        if tmp_contribuicao >=30:
            '''Se o gênero definido for Mulher, ele verifica o tempo 
            de contribuição necessario para mulheres se aposentar
            e validara a aposentadoria.''' 
            print(f"Senhora {nome} sua aposentadoria foi validada.")
            if tmp_contribuicao<30:
                #Se for menor do que o necessario, será invalidada. 
                print(f"Senhorita {nome} sua aposentadoria não foi validada.")
    '''Se o gênero definido for Homem o código verifica se o valor da variavel genero é 1,
        e verifica se o valor atribuido é realmente 1.'''
    if genero ==1:
        if tmp_contribuicao >=35:
            '''Se o gênero definido for Homem, ele verifica o tempo 
            de contribuição necessario para homens se aposentar
            e validara a aposentadoria.''' 
            print(f"Senhor {nome} sua aposentadoria foi validada.")
        if tmp_contribuicao<35:
            """Se for menor do que o tempo atribuido, será invalidado """
            print(f"Senhor {nome} sua aposentadoria não foi validada.")
   































    







