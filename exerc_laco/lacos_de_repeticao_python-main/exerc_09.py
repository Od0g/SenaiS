numero = int(input("Informe um número: "))
resultado = 0

if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif ((numero == 0) or (numero == 1)):
    print(1)
else:
    resultado = 1
    for i in range(2, numero + 1):
        resultado = resultado * i
        

print(resultado)

