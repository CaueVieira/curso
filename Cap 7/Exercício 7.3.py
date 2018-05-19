"""Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem em uma delas.

1ª String: CTA
2ª String: ABC
3ª String:  BT  """

String1 = 'CTA'
String2 = 'ABC'
String3 = []

for letra in String1:
    if letra in String1 and letra in String2:
        next
    else:
        String3.insert(0, letra)

for letra in String2:
    if letra in String1 and letra in String2:
        next
    else:
        String3.insert(0, letra)

print(String3)