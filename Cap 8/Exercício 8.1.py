"""Escreva uma função que retorne o maior de nois números"""


def maximo(x, y):
    if x == y:
        return("Os dois números são iguais.")
    return x if x > y else y


print(maximo(7, 7))
