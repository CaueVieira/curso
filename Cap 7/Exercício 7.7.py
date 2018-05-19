# Modifique o programa de forma a escrever a palavra secreta caso o jogador perca

palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(100):
     print()
digitadas = []
acertos = []
erros = 0
boneco = ["  |   ", " \|   ", " \|/  "]
boneco2 = [" /     ", " / \ "]

while True:
    senha = ""
    for letra in palavra:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == palavra:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
              acertos += tentativa
        else:
              erros += 1
              print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    print("X%s" % boneco[erros-2]) if erros >=2 and erros <5 else next
     print("X{}\nX{}".format(boneco[2],boneco2[erros-5])) if erros >=5 else next
    print("X\n===========")
    if erros == 6:
       print("Enforcado!")
        print("A palavra secreta é '{}'".format(palavra))
         break
