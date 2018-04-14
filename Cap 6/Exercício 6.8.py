"""Modifique o primeiro exemplo (Listagem 6.23) de forma a realizar a mesma tarefa, mas sem utilizar a variável "achou". Dica: Observe
a condição de saída do while"""

L = [15,7,27,39]
p = int(input("Digite o valor a procurar\n"))
x = 0

while x < len(L):
    if L[x] == p:
        print("{} achado na posição {}".format(p, x))
        break
    x += 1

else:
    print ("{} não encontrado".format(p))
