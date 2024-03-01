import time
import os

# A fórmula dos juros compostos é a seguinte:

# FV = PV*(1+i) elevado a n

# Onde:
# FV = Valor final do investimento, ao término do tempo
# PV = Valor inicial que o cliente irá investir
# i = Rentabilidade mensal (em percentual)
# n = Quantidade de meses que o dinheiro do cliente vai ficar aplicado


# Elabore um Script em linguagem Python que solicite o valor do investimento (PV), o número de meses(n)
# que irá permanecer aplicado e rentabilidade (i). Ao final, o script deve mostrar o valor 
# do montante total (FV)

print('Preencha os dados a seguir senhor cliente: ')
pv = float(input('Investimento Inicial: '))
n = int(input('Número de meses que deseja permanecer aplicado: '))
i = float(input('Rentabilidade: '))

os.system('cls')
print('Aguarde um momento, o montante esta sendo processado...')
time.sleep(4)

p1 = (1+(i/100))
p2 = pow(p1, n)
p3 = pv * p2

print('O seu montante total é de:', p3)