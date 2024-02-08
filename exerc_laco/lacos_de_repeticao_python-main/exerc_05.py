numero = 0
resultado = 0

while(numero != -1):
    numero = float(input("Infome um numero: "))
    if(numero == -1):
        break
    else:
        resultado = resultado + numero
        print("Resultado: ",resultado)

print("Resultado Final: ",resultado)