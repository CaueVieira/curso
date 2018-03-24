"""Escrev um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0(zero).
No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética"""

s = 0
n = int(0)

while True:
    v = int(input("Digite um número ou 0 para sair:"))
    if v == 0:
        break
    s = s+v
    n = n + 1

media = s / n

print ("Soma: {} \nQuantidade de números digitados: {} \n Média aritmética: {}".format(s, n, media))