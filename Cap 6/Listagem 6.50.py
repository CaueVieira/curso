estoque ={"Alface": [500 , 0.45],
          "Batata": [2001, 1.20],
          "Tomate": [1000, 2.30],
          "Feijão": [100 , 1.50]}

venda = [ ["Tomate",  5],
          ["Batata", 10],
          ["Alface",  5]]
total = 0

print ("Vendas:\n")
for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print("{}: {} x {} = {}".format(produto,quantidade,preco,custo))
    estoque[produto][0] -=quantidade
    total+=custo
print ("Custo total: {}\n".format(total))
print("Estoque:\n")
for chave, dados in estoque.items():
    print ("Descrição: ", chave)
    print ("Quantidade: ", dados[0])
    print ("Preço: {}".format(dados[1]))










