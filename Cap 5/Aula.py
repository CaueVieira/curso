import time
from doctest import master

"""x = 3
fim = 10
count = 1
while count <= 10:
    if x % 3 == 0:
        print (x)
        count = count + 1
    x = x + 1"""


"""pontos = 0
questao = 1

while questao <= 3:
    resposta = input("Resposta da questão {}: ".format(questao))
    if questao == 1 and resposta == "b" or "B":
        pontos +=1
    if questao == 2 and resposta == "a" or "A":
        pontos += 1
    if questao == 3 and resposta == "d" or "D":
        pontos += 1
    questao +=1
print ("O aluno fez {} ponto(s)".format(pontos))"""

tabuada=1
while tabuada <= 10:
    número = 1
    while número <= 10:
        print ("%d x %d = %d" % (tabuada, número, tabuada * número))
        número+=1
    tabuada+=1