numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

numeroMenor = 0
numeroMaior = 0

while(numero1 == numero2):
    print("Números são iguais. Insira um números que são diferentes")
    numero1 = int(input("Informe novamente o primeiro número: "))
    numero2 = int(input("Informe novamente o segundo número: "))

    if (numero1 != numero2):
        break

if(numero1 > numero2):
    numeroMaior = numero1
    numeroMenor = numero2
    
elif (numero2 > numero1):
    numeroMaior = numero2
    numeroMenor = numero1

print(f"Números contidos entre {numeroMenor} e {numeroMaior}")
for i in range(numeroMenor+1, numeroMaior, 1):
    print(i)

