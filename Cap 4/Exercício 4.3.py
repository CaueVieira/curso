"""Escreva um programa que leia três números e que iprima o maior e o menor"""

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
maior = 0
menor = 0

if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > b and c > a:
    maior = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < b and c < a:
    menor = c

print ("Menor: %d - Maior: %d" % (menor, maior))