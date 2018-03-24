"""Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km
para viagens de até 200 km e R$ 0,45 para vigens mais longas"""

print ("Calculadora de preços com base em Kms percorridos em viagem")

kms = float(input("Informe distância em Kms:"))
preco = 0

if kms <= 200:
    preco = kms * 0.5

else:
    preco = kms * 0.45

print ("O preço da passagem é de R$%5.2f" % (preco))






