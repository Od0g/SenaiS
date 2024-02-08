valor_tabuada = int(input(" Informe qual o valor da tabuada: "))

for i in range(1,11,1):
    resultado = i * valor_tabuada
    print(f"{valor_tabuada} x {i} = {resultado}")