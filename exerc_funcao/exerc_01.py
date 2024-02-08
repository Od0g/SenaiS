def calcular_media(nota1, nota2, nota3):
    media = (nota1+nota2+nota3)/3

    return round(media,2)

def main():
    nota1=float(input("informe a primeira nota:"))
    nota2=float(input("informe a segunda nota:"))
    nota3=float(input("informe a terceira nota:"))

    resultado=calcular_media(nota1, nota2, nota3)
    print(f" Calculo da média: {resultado} ")
    
if __name__=="__main__":
    main()