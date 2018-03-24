"""Escreva um programa que leia dois números e que pergunta qual operação você deseja realizar. Você deve poder calcular a soma, subtração,
multiplicação e divisão. Exiba o resultado da operação solicitada."""

op = str(input("Que operação deseja realizar? (+ , - , *, /): "))
a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))
resultado = 0

if op == "+":
    resultado = a + b
elif op == "-":
    resultado = a - b
elif op == "*":
    resultado = a * b
elif op == "/":
    resultado = a / b
else:
    print ("Opção incorreta")

print ("Total = %5.2f" % resultado)


