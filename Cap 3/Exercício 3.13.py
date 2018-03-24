"""Escreva um programa que converta uma tempertura digitada em Cº em Fº."""

print ("Conversor de temperatura. Informe a temperatura em Celsius")

C = float(input("Digite a temperatura em Celsius: "))
F = (9*C)/5 + 32

print ("\n %5.2fºC equivale a %5.2fºF" % (C,F))