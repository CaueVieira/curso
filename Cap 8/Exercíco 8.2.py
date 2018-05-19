# Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo


def multiplicador(a, b):
    return a % b == 0

a, b = input("Coloque dois números, separados por espaço:\n").split()
a, b = int(a), int(b)
print(multiplicador(a, b))
