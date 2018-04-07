"""Altere o programa da listagem 6.21 de forma a poder trabalhar com vários comandos digitados de uma só vez.
Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação como uma string.

Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a saída do programa."""

último = 10
fila = list(range(1, último+1))
n = 0
while True:
    n = 0
    print("\nExistem {} clientes na fila".format(len(fila)))
    print ("Fila atual:", fila)
    print ("Digite F para adicionar um cliente ao fim da fila, ou A para realizar o atendimento. S para sair.")
    operação = str(input("\nOperação (F, A ou S):"))
    for k in operação:
        if operação[n] == "A":
            if(len(fila))>0:
                atendido = fila.pop()
                print("Cliente {} atendido".format(atendido))
            else:
                print ("Fila vazia! Ninguém para atender.")
        elif operação[n] == "F":
            último = len(fila) + 1 # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação[n] == "S":
            break
        else:
            print ("Operação inválida! Digite apenas F, A, ou S!")
        n+=1