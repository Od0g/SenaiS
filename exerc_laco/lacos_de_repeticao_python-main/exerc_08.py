
numero = int(input("Digite um número inteiro: "))
resto = 0

for i in range(2, numero):
    resto = numero % i

    # Se o resto for 0, o número não é primo, pois é divisível por i
    if resto == 0:
        print(f"{numero} não é um número primo.")

print(f"{numero} é um número primo.")





