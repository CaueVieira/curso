"""Altere o programa da listagem 6.53 de forma a solicitar ao usuário o produto e a quantidade vendida. Verifique se o nome do produto digitado
existe no dicionário, e só então efetue a baixa em estoque."""

estoque ={"alface": [500 , 0.45],
          "batata": [2001, 1.20],
          "tomate": [1000, 2.30],
          "feijão": [100 , 1.50]}

total = 0

print ("Vendas:\n")

while True:
    produto = input("Digite o produto vendido, ou fim para sair: ").lower()
    if produto == "fim":
        break
    elif produto in estoque:
        preco = estoque[produto][1]
        quantidade = float(input("Digite a quantidade vendida: "))
        if quantidade > estoque[produto][0]:
            print ("O estoque é menor que a quantidade vendida")
        else:
            custo = preco * quantidade
            print("{}: {} x R$ {:6.2f} = R$ {:6.2f}".format(produto,quantidade,preco,custo))
            estoque[produto][0] -=quantidade
            total+=custo
    else:
        print("Produto não está no estoque")

print ("Custo total: {:6.2f}\n".format(total))
print("Estoque:\n")

def printEstoque(itemsDict, leftWidth, rightWidth):
    print ("ESTOQUE".center(leftWidth + rightWidth, '-'))
    for chave, dados in estoque.items():
        print ("Descrição".ljust(leftWidth, '.'), chave.capitalize())
        print ("Quantidade".ljust(leftWidth, '.'), int(dados[0]))
        print ("Preço".ljust(leftWidth, '.')+" R$ {:2.2f}".format((dados[1])))
        print ("")
printEstoque(estoque, 20,7)









