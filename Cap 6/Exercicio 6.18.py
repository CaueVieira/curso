"""Escreva um programa que gere um dicionario, onde cada chave seja um caractere e seu valor seja o número desse caractere encontrando em uma frase lida."""
import pprint

dicionario = {}
frase = str(input("Digite uma frase: "))

for caracteres in frase:
    dicionario.setdefault(caracteres, 1)
    dicionario[caracteres] += 1

pprint.pprint(dicionario)

[================================y]