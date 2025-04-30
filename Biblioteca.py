def imprimeNome(nome):
    print(f"Nome:^{nome}")
def solicitarNome():
    nome=input("Digite seu nome: ")
    return nome
def piramide(num):
    for u in range(1, num + 1, 1):
        for y in range(0, u):
            print(u, end=" ")
        print()
def conteVogais(text):
    cont = 0
    vogais = "aeiouAEIOU"
    for x in range(len(text)):
        if text[x] in vogais:
            cont = cont + 1
    print(cont)
def valorTotalestoque(produto, valorUnitario, quantidade):
    valorTotal = valorUnitario * quantidade

def numero(num):
    if num!=0:
        if num>0:
            return "P"
        else:
            return "N"
    else:
        return "Z"
