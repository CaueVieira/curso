"""Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro cust R$ 60 por dia e R$ 0,15 por km rodado."""

dias = int(input("Quantidade de dias com o carro: "))
km = float(input("Kms rodados: "))
preco_a_pagar = dias * 60 + 0.15 * km
print ("O preço a pagar é de R$ %5.2f" % preco_a_pagar)