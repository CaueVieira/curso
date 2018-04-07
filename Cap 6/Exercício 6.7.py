"""Faça um programa que leia uma expressão com parênteses. Usando pilhas, verifique se os parentêses foram abertos e fechados
na ordem correta. Exemplo:

(())        ok
()()(()())  ok
())         erro """

expressao = input("Digite sequencia de parenteses para validar: ")
n = 0
pilha = []

for k in expressao:
    if expressao[n] == "(":
        pilha.append("(")
    if expressao[n] == ")":
        if len(pilha)>0:
            pilha.pop(-1)
        else:
            pilha.append(")")
            break
    n+=1

print("OK") if len(pilha) == 0 else print("Erro")