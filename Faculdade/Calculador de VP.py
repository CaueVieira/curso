"""Calcula o VPL de um investimento dado os inputs do usuário"""

"""Calcule o VPL e a TIR do projeto abaixo, antes e depois
do imposto de renda. Suponha uma TMA de 20%, uma
alíquota de 34% de imposto de renda e que o
investimento inicial se deprecie em 5 anos, linearmente.
Ano FC
0 -1500
1 300
2 450
3 750
4 750
5 900"""

x = 1
investimento = float(input("Insira o valor do investimento:\n"))
n = int(input("Insira o número de períodos\n"))
VPL = 0
tributacao = 0
depreciacao = investimento * 0.2
VPLi = 0

while x <= n:
    periodo = float((input("Insira a rentabilidade do período {}: ".format(x))))
    lucroTributavel = periodo - depreciacao
    if lucroTributavel < 0:
        lucroTributavel = 0
    imposto = lucroTributavel * 0.34
    posImposto = periodo - imposto
    VPLperiodo = periodo / 1.20 ** x
    VPLimposto = posImposto / 1.20 ** x
    VPL = VPL + VPLperiodo
    VPLi = VPLimposto + VPLi
    x += 1


print("VPL final, antes do imposto de renda = {0:.2f}".format(VPL-investimento))
print("VPL final, após imposto de renda     = {0:.2f}".format(VPLi-investimento))