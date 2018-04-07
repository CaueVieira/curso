import pprint

codigo = 0
quantidade = 0
custo = 0
soma = 0


preco = {1: 0.50, 2: 1, 3:4, 5:7, 9:9}

while True:
    codigo = int(input("Digite o codigo do produto: "))
    if codigo == 0:
        break
    elif codigo in preco:
        quantidade = int(input("Digite a quantidade comprada: "))
        custo = quantidade * preco[codigo]
        soma = soma + custo
    else:
        print ("Codigo inválido")

pprint.pprint(preco)
print ("Você gastará R${:5.2f} nesta compra".format(soma))