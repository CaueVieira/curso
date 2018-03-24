""""Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunta a quantidade de kWh consumida e o tipo de
energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residÊncias, I para ind´sutrias, C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir"""

kWh = int(input("Consumo: "))
instalacao = input("Tipo de instalação (R, C ou I): ")
preco = 0

if instalacao == "R" or instalacao == "r":
    if kWh < 500:
        preco = kWh * 0.4
    else:
        preco = kWh * 0.65

elif instalacao == "C" or instalacao == "c":
    if kWh < 1000:
        preco = kWh * 0.55
    else:
        preco = kWh * 0.6

elif instalacao == "I" or instalacao == "i":
    if kWh < 5000:
        preco = kWh * 0.55
    else:
        preco = kWh * 0.6

if preco > 0:
print ("Você consumiu {:d}, portanto o preço a pagar é de R$ {:05.2f}".format(kWh, preco))

else:
    print ("Apenas se aceita instalação = R, C ou I")

