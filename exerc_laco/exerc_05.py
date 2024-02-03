print("----Conversor de C° para K° e F°.-----")
grau_c = float(input("Digite a Temperatura em C°: "))

f = float((9 * grau_c) / 5) + 32
k = float(grau_c+273)


opcao = int(input("""Qual temperatura deseja converter 
[K]/1
[F]/2
"""))
if opcao == 1:
    print(f'A temperatura em kelvin: {k}°K.')
if opcao == 2:
    print(f'A temperatura em fahrenheit: {f}°F.')


