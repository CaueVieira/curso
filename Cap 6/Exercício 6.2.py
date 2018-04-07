"""Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras."""

A = []
B = []
while True:
    print ("Digite valores para a primeira lista, ou 0 para sair")
    ItensA = int(input ())
    if ItensA == 0:
        break
    else:
        A.append(ItensA)

while True:
    print("Digite valores para a segunda lista, ou 0 para sair")
    ItensB = int(input())
    if ItensB == 0:
        break
    else:
        B.append(ItensB)

C = A+B
print ("A+B = {}".format(C))