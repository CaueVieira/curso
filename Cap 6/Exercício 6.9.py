"""Modifique o exemplo para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também será procurado. Na impressão
indique qual dos dois valores foi achado primeiro."""

Lista = [15, 7, 27, 39]
pesquisa1 = int(input("Digite o primeiro valor a procurar\n"))
pesquisa2 = int(input("Digite o segundo valor a procurar\n"))
x = 0
achouP = False
achouV = False
contPesquisa1 = 0
contPesquisa2 = 0

for numeros in Lista:
    if Lista[x] == pesquisa1:
        achouP = True
        contPesquisa1 = x # Trava o contador para depois testar qual vem primeiro.
        if pesquisa2 not in Lista:
            print("Primeira pesquisa: Valor de {} encontrado na posição {}. \nSegundo valor pesquisado não foi encontrado.".format(pesquisa1, contPesquisa1))
    if Lista[x] == pesquisa2:
        achouV = True
        contPesquisa2 = x # Trava o contador para depois testar qual vem primeiro.
        if pesquisa1 not in Lista:
            print("Segunda pesquisa: Valor de {} encontrado na posição {}. \nPrimeiro valor pesquisado não foi encontrado.".format(pesquisa2, contPesquisa2))
    x += 1

if achouP == False and achouV == False:
    print ("Nenhum dos valores foram encontrados.")
elif achouP == True and achouV == True:
    print("Primeira pesquisa: Valor de {} encontrado na posição {}.".format(pesquisa1, contPesquisa1))
    print("Segunda pesquisa: Valor de {} encontrado na posição {}.".format(pesquisa2, contPesquisa2))
    if contPesquisa1 < contPesquisa2:
        print ("A primeira pesquisa foi encontrada primeiro.")
    elif contPesquisa1 == contPesquisa2:
        print ("As duas pesquisas são iguais.")
    else:
        print("A segunda pesquisa encontrada primeiro.")