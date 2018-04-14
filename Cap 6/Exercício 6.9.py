"""Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado. Na impressão
indique qual dos dois valores foi achado primeiro."""

L = [15,7,27,39]
p = int(input("Digite o primeiro valor a procurar\n"))
v = int(input("Digite o segundo valor a procurar\n"))
x = 0
y = 0
achouP = False
achouV = False
a = 0
b = 0

for numeros in L:
    if L[x] == p:
        achouP = True
        a = x
        if v not in L:
            print("Primeira pesquisa: Valor de {} encontrado na posição {}. \nSegundo valor pesquisado não foi encontrado.".format(p, a))
    if L[x] == v:
        achouV = True
        b = x
        if p not in L:
            print("Segunda pesquisa: Valor de {} encontrado na posição {}. \nPrimeiro valor pesquisado não foi encontrado.".format(v, b))
    x += 1

if achouP == False and achouV == False:
    print ("Nenhum dos valores foram encontrados.")
elif achouP == True and achouV == True:
    print("Primeira pesquisa: Valor de {} encontrado na posição {}.".format(p, a))
    print("Segunda pesquisa: Valor de {} encontrado na posição {}.".format(v, b))
    if a < b:
        print ("A primeira pesquisa foi encontrada primeiro.")
    elif a == b:
        print ("As duas pesquisas são iguais.")
    else:
        print("A segunda pesquisa encontrada primeiro.")