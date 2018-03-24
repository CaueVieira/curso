
"""Escreva um programa para calcular a redução do tempo de vida de um fumante. PErgunte a qunatidade de cigarros fumados por dia e quantos
anos ele já fumou. Considere que um fumanete perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba
o total em dias."""

print ("Calculador de tempo de vida perdido fumando")

quantidade = int(input("Informe a quantidade de cigarros fumados por dia: "))
tempo = int(input("Informe quantos anos você é fumante: "))

cigarrosFumados = quantidade * (365 * tempo) #Calcula o total de cigarros fumados
tempoPerdido = cigarrosFumados * 10 #Vai me dar o tempo em minutos
tempoPerdidoDias = tempoPerdido / 60 / 24

print ("Você já perdeu %d dias de vida." % tempoPerdidoDias)
