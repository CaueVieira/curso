"""Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um
aumento de 10%. Para os inferiores ou iguais, de 15%"""

print("Calculadora de aumento de salário")

salari = float(input("Informe seu salário: "))
salario = salari
porcentagemAumento = 0.15

if salario > 1250:
    porcentagemAumento = 0.10
    salario = porcentagemAumento * salario
    print ("Aumento de R$ %5.2f" % salario)
if salario < 1250:
    salario = porcentagemAumento * salario
    print ("Aumento de R$ %5.2f" % salario)
    print (porcentagemAumento)

