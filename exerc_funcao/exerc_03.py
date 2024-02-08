def resultado_sum(num1, num2):
    soma = num1+num2

    return soma

def resultado_sub(num1, num2):
    subtracao = num1+num2

    return subtracao

def resultado_div(num1, num2):
    divisao = num1/num2

    return divisao

def resultado_mult(num1, num2):
    multiplicacao = num1+num2

    return multiplicacao




def main():
    num1 = int(input("Digite o primeiro número:"))
    num2 = int(input("Digite o segundo número:"))

    resultado1= resultado_sum(num1, num2)
    resultado2= resultado_sub(num1, num2)
    resultado3= resultado_div(num1, num2)
    resultado4= resultado_mult(num1, num2)

    print(f"""  
A soma entre {num1} e {num2} é {resultado1}          
A subtração entre {num1} e {num2} é {resultado2}            
A divisão entre {num1} e {num2} é {resultado3}
A multiplicão entre {num1} e {num2} é {resultado4}              
          """)


if __name__=="__main__":
    main()

