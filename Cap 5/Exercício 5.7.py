import time

time.sleep(2)
print ("CALCULADOR DE TABUADA DE 7")
x = int(input("Começo da tabuada: "))
y = x * 7
fim = int(input("Fim da tabuada: "))
count = 1
while x <= fim:
    print ("{} x 7 = {}".format(x,y))
    count = count + 1
    x = x + 1
    y = x * 7
    time.sleep(1)