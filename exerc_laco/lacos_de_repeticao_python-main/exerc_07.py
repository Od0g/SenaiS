dividendo = int(input("Informe um número: "))

divisor = 2
resto = 0

while dividendo > 1:
    resto = dividendo % divisor
    
    # Se o resto for igual a 0, significa que o divisor é um fator primo do dividendo
    if resto == 0:
        print(divisor)
        
        # Atualiza o dividendo dividindo-o pelo divisor
        dividendo = dividendo / divisor
    
    # Se o resto não for igual a 0, incrementa o divisor para verificar o próximo número
    else:
        divisor = divisor + 1

