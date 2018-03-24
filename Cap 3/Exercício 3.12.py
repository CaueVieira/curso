"""Escreva um programa que calcule o tempo de uma viagem de carro. Pegunte a distância a percorrer e a velocidade média esperada para a viagem"""

print("Calculadora de tempo de viagem! Informe a distância a percorrer e a velocidade média esperada para a viagem")

distancia = int(input("Distancia a percorrer (em km): "))
velocidade = int(input("Velocidade média esperada (em km/h): "))
tempo = distancia / velocidade
tempo_s = int(tempo * 3600) # Converte horas para segundos
horas = int(tempo_s / 3600) # Separa a parte inteira (horas)
tempo_s = int(tempo_s % 3600) # Separando o resto
minutos = int(tempo_s / 60)
segundos = int(tempo_s % 60)

print("Você levara %d horas e %d minutos para percorrer %d kms" % (horas, minutos, distancia))

