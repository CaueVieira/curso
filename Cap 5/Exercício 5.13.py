"""Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago.
Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago"""

DividaInicial = float(input("Divida inicial: "))
TaxaJuros = float(input("Taxa de juros: ")) / 100
MensalPago = float(input("Mensal pago: "))
Inicio = DividaInicial
Mes = 1

if (DividaInicial * TaxaJuros) > MensalPago:
    print ("Não vais pagar tua dívida nunca desse jeito Ô meu quirido")
else:
    while DividaInicial > 0:
        DividaAtualizada = DividaInicial + (DividaInicial * TaxaJuros)
        DividaInicial = DividaAtualizada - MensalPago
        Mes = Mes + 1

    pago = MensalPago * Mes
    juros = pago - Inicio + DividaInicial

    print ("Você pagará sua dívida em {} meses. O total pago é de R${:06.2f}, sendo R${:06.2f} em juros".format(Mes, pago, juros))




