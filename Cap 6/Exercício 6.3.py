"""Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos."""

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
    elif ItensB in A:
        ItensB = ""
    else:
        B.append(ItensB)

C = A+B
C.sort()
print ("A+B = {}".format(C))

