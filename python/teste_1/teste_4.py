import random

n1 = str(input('Nome1: '))
n2 = str(input('Nome2: '))
n3 = str(input('Nome3: '))
n4 = str(input('Nome4: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print(lista)