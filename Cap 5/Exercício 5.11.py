"""Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma aplicação. Exiba os valores mês a mês para os 24 primeiros meses.
Escreva o total ganho com juros no período"""

deposito = float(input("Deposito inicial: "))
juros = float(input("Taxa de juros: ")) / 100
prazo = int(input("Prazo do deposito: "))
depositoMensal = float(input("Deposito mensal: "))
x = deposito
soma = 0
n = 1

while n <= prazo:
    deposito = deposito + depositoMensal + (deposito * juros)
    print("Saldo no mês {} é de R$ {:06.2f}".format(n,deposito))
    n += 1

rendimento = deposito - x - (depositoMensal * prazo)

print ("Você recebeu R${:06.2f} em juros, saldo final de R${:06.2f}".format(rendimento, deposito))