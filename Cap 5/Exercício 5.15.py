codigo = 0
quantidade = 0
custo = 0
acumulado = 0
soma = 0
preco = 0



while True:
    def calculadora(preco):
        quantidade = int(input("Digite a quantidade comprada: "))
        custo = quantidade * preco
        soma = 0
        soma = soma + custo
    codigo = int(input("Digite o codigo do produto: "))
    if codigo == 0:
        break
    elif codigo == 1:
        calculadora(0.50)
    elif codigo == 2:
        calculadora(1)
    elif codigo == 3:
        calculadora(4)
    elif codigo == 5:
        calculadora(7)
    elif codigo == 9:
        calculadora(9)
    else:
        print ("Codigo inválido")

print ("Você gastará R${:6.2f} comprando essas bagaças aí".format(soma))