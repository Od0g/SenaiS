
def vogais(string):
    vagais="aeiouAEIOU"
    qtdd_vogais = 0
    for i in string:
        if i in vagais:
            qtdd_vogais = qtdd_vogais+1

    return print(f"foram encontradas {qtdd_vogais} vogais.")

def main():
    string=input("Digite sua frase:")

    resultado=vogais(string)
    #print(f"foram encontradas {resultado} vogais.")

if __name__=="__main__":
    main()