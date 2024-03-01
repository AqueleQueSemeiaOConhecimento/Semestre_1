import time
import os

# Suponha que o preço da capa de um livro seja R$24,95, mas as livrarias recebem um desconto
# de 35%. O transporte custa R$3,00 para o primeiro exemplar e 75 centavos para cada exemplar
# adicional. Qual é o custo total de cada X cópias? solicite o valor de X. Crie um Script em 
# linguagem Python para solicitar os dados necessários e exibir o custo total da compra.

print('Deseja comprar um livro conosco?')
time.sleep(2)

print('Digite 1 para efetuar uma compra e qualquer numero para encerar a compra')
x = int(input('Digite aqui: '))


def switch(x):
    match x:
        case 1:
            time.sleep(1)
            os.system('cls')
            try:
                num_livro = 0
                num_livro = int(input('Digite o número de livros que deseja comprar: '))
                num_livro -= 1
                valor_livro = (24.95 * 1.35) + 3 + (num_livro * 0.75)
                print('Valor do livro é: ', valor_livro)
            
            except ZeroDivisionError:
                print('Valor inserido invalido')
                
        case default:
            os.system('cls')
            print('Muito obrigado, volte sempre')
            time.sleep(2)
            os.system('cls')
            
switch(x)
        
        

