"""Escreva um programa que calcule o aumento de salário. ELe deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
e do novo salário"""

print ("\n CALCULADORA DE SALÁRIOS - Escreva seu salário e o aumento em porcentagem \n")
salario = float(input("Seu salário: "))
aumento = int(input("Aumento (em %): "))
taxa_aumento = aumento / 100 # Transforma o valor do usuário em porcentagem
valor_aumento = salario * taxa_aumento
novo_salario = salario + valor_aumento
print("\n Você recebeu um aumento de R$ %5.2f! Seu novo salário é de R$ %5.2f" % (valor_aumento, novo_salario))