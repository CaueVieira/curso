# Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo


def multiplicador(a, b):
    return True if b % a == 0 else "Não é multiplo"


print(multiplicador(7, 3))
