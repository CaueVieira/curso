"""Escreve um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário
foi multado. Nese caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80km/h."""

velocidade = int(input("Velocidade do carro: "))
if velocidade > 80:
    valor_da_multa = (velocidade - 80) * 5
    print ("Você foi multado! O valor da multa é de R$ %d" % (valor_da_multa))
else:
    print ("Você está dentro da lei.")