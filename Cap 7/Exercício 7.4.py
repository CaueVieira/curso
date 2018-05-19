"""Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string.

String: TTAAC"""

import pprint

String = 'TTAAC'
Dict = {}

for letra in String:
    Dict.setdefault(letra, 0)
    Dict[letra] += 1

pprint.pprint(pprint.pformat(Dict))
