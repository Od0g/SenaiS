
def verifica_se_par(numero):
    resto = numero % 2

    if resto == 0:
        print(True)
    else:
        print(False)
    
    return resto



def main():
    print("=======Verificador de Números pares======")
    numero = float(input('Digite um número :'))
    resultado=verifica_se_par(numero)
    
if __name__=="__main__":
    main()