"""Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário
e a quantidade de anos a pagar. O valor da prestação mensal não pode ser super a 30% do salário. Calcule o valor da prestação como sendo o valor
da casa a comprar dividido pelo número de meses a pagar."""

valorCasa = float(input("Valor da casa: "))
salario = float(input("Valor do salário: "))
anos = float(input("Anos de empréstimo: "))
prestacao = valorCasa / (anos * 120)


if prestacao < (salario * 0.3):
    print ("A prestação é de R$ {:05.2f}".format(prestacao)
    print ("Emprestimo aprovado.")
else:
    print ("Emprestimo negado.")
