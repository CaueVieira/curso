"""Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar"""

print("Calculadora de desconto - Informe o preço da mercado e o percentual de desconto \n")

mercadoria = float(input("Preço do produto: "))
desconto = float(input("Porcentual de desconto (escreva só números): "))
valor_desconto = mercadoria * (%desconto/100)
novo_preco = mercadoria - valor_desconto

print("Você recebeu um desconto de %5.2f! O preço com desconto é de R$ %5.2f" % (valor_desconto, novo_preco))