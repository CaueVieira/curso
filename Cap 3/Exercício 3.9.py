"""Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos"""

#Um minuto = 60 segundos
#Uma hora  = 3600 segundos
# Um dia tem 24 horas, logo 24 * 3600 segundos

dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))
print ("O total em segundos é de "+ str((segundos + minutos * 60 + horas * 3600 + dias * (3600 * 24))))