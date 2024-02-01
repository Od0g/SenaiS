# Calculo da Área de um Círculo

from math import pi

raio = float(input("Digite o raio do Círculo: "))

area = pi * ((raio)**2)

print(area)

"""0

Para pegar o número por inteiro, você deve usar uma “string” formatada, ou seja, para determinar o modo como ele sera printado na tela:

O tipo "float" pode ser formatado destas formas:

:.0f # sem zeros a esquerda
:.2f # com dois zeros
Obs: pode se colocar mais do que 2 apenas.

Neste caso

a = 8682372684397235357614080000
b = 86400

c = a/b # divisão normal

print(f"{c:.0f}") # :.0f sem zeros a esquerda"""