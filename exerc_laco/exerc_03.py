print("------Tabuada-------")
'''O usuário insere um valor desejado, exemplo:
1, 2 , 3...,
e armazenamos na variável 'valor_tabuada'.'''
valor_tabuada = int(input("Digite o valor da tabuada: "))
'''Em seguida, usamos uma variável "i" que vai de 0 até 10 dentro do laço FOR e função range.'''
for i in range(10):
    print(f'{valor_tabuada} x {i} = {valor_tabuada*i}')

