numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

while(numero1 == numero2):
    print(" -- Não são aceitos números iguais --")
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))
    if(numero1 != numero2):
        break

maior_numero = 0
menor_numero = 0

if(numero1 > numero2):
    maior_numero = numero1
    menor_numero = numero2
else:
    maior_numero = numero2
    menor_numero = numero1

resto = 0
contador_impar = 0
contador_par = 0

for i in range (menor_numero, maior_numero+1, 1):
    resto = i % 2
    if(resto != 0):
        contador_impar = contador_impar + 1
    else:
        contador_par = contador_par + 1

print(f"Quantidade de númeres pares {contador_par}")
print(f"Quantidade de númeres ímpares {contador_impar}")