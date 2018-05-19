# Escreva uma função que receba o lado(L) de um quadrado e retorne sua área (A = lado²)


def area_quadrado(x):
    return x ** 2


while True:
    x = int(input("Digite o número para descobrir a área do quadrado, ou 0 para sair:\n"))
    if x == 0:
        break
    else:
        print(area_quadrado(x))
