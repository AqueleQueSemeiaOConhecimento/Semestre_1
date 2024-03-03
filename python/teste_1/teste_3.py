# biblioteca random
import random
# ou from random import choice

n1 = str(input('Nome 1: '))
n2 = str(input('Nome 2: '))
n3 = str(input('Nome 3: '))
n4 = str(input('Nome 4: '))

lista = [n1, n2, n3, n4]

# random.choice(array) sorteia um elemento do array
escolhido = random.choice(lista)

print(f'Aluno escolhido foi {escolhido}')