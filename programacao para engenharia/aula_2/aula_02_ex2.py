import os
import time

# Ainda sobre juros composto. Um cliente pediu que o sistema do banco tivesse a seguinte função:

# Informar o valor inicial que ele deve investir, para o final de 'n' meses ele tenha um valor de 'fv',
# supondo que este dinheiro esteja com uma rentabilidade 'i' mensal, em porcentagem

# Desenvolva um script em linguagem Python que solicite o valor final, o número de meses
# que retende deixar seu dinheiro aplicado, bem como a rentabilidade. O script deve
# exibir i valor inicial que ele deve investir para atingir tal objetivo.

# PV = FV / (1+i) sobre potencia de n


print('Preencha os dados a seguir senhor cliente: ')
fv = float(input('valor desejado: '))
n = int(input('Número de meses que deseja permanecer aplicado: '))
i = float(input('Rentabilidade: '))

os.system('cls')
print('Aguarde um momento, o montante esta sendo processado...')
time.sleep(4)

p1 = (1+(i/100))
p2 = pow(p1, n)
p3 = float(fv / p2)
p4 = "{:.2f}".format(p3)

print('Para o valor desejado dado os dados sera preciso aplicar:' + str(p4) + ' reais')