"""Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.

1ª String: AAACTBF
2ª String: CBT                                                                                              """

String1 = 'AAACTBF'
String2 = 'CBT'
String3 = []

for letras in String2:
    String3.insert(len(String3), letras) if letras in String1 else next

print (String3)