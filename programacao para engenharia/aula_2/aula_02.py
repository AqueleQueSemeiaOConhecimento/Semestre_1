import os

# ============================================================================================

# Soma de 2 números

# a = 10
# b = 20

# soma = a + b

# print('Soma dos numeros: ', soma)


# ===========================================================================================

x = 0

# x = int(input('Insira um valor'))

# if x%2 :
#     print('number is impar')

# else :
#     print('numer is par')


# ==================================================================================================

# # Defina uma variável com a string desejada
# minha_string = "Olá, mundo!"

# # Use a função len() para contar o número de caracteres na string
# num_caracteres = len(minha_string)

# # Exiba o número de caracteres no console
# print("O número de caracteres na string é:", num_caracteres)


# print(minha_string)

# uper = minha_string.upper()

# print(uper)


# ===============================================================================================

# print('Veja agora a sua string de diferentes formas')
# string_for_me = str(input('Insira um texto: '))

# upper_case = string_for_me.upper()

# lower_case = string_for_me.lower()

# lenght_for_string = len(string_for_me)

# print('Tudo em maiusculo: ', upper_case)
# print('Tudo em minusculo: ', lower_case)
# print('Comprimento da string: ', lenght_for_string)

# ===========================================================================================

# for i in range(10):
#     print(i)
    

# ============================================================

# print('Calculadora Simples')
# print('1 = Soma')
# print('2 = Subtração')
# print('3 Multiplicação')
# print('4 Divisão')

# number = int(input('Insira aqui o número: '))

# def switch(x):
#     match x:
#         case 1:
#             os.system('cls')
#             print('Soma')
#             num1 = float(input('Insira um numero: '))
#             num2 = float(input('Insira outro numero: '))
#             operacao = num1 + num2
#             print('A soma de ' + str(num1) + ' o número ' + str(num2) + ' é igual a :', operacao)
            
#         case 2:
#             print('Subtração')
#             os.system('cls')
#             print('Subtração')
#             num1 = float(input('Insira um número: '))
#             num2 = float(input('Insira outro numero: '))
#             operacao = num1 - num2
#             print('A subtração de ' + str(num1) + ' pelo numero ' + str(num2) + ' é igual a: ', operacao)
            
#         case 3:
#             print('Multiplicação')
#             os.system('cls')
#             print('Subtração')
#             num1 = float(input('Insira um número: '))
#             num2 = float(input('Insira outro numero: '))
#             operacao = num1 * num2
#             print('A multiplicação do numero ' + str(num1) + ' pelo numero ' + str(num2) + 'é igual a: ', operacao)
        
#         case 4:
#             print('Divisão')
#             os.system('cls')
#             print('Divisão')
#             num1 = float(input('Insira um número: '))
#             num2 = float(input('Insira outro numero: '))
#             operacao = num1 / num2
#             print('A divisão de ' + str(num1) + ' pelo numero ' + str(num2) + ' é igual a: ', operacao)
            
#         case default:
#             print('Numero invalido')

# switch(number)

# ======================================================================================

# Aluno aprovado ou não

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

os.system('cls')

if media >= 6:
    print('Aluno Aprovado com media de ' + str(media))
    
else:
    media_passar = 6 - media
    print('Aluno Reprovado por falta de ' + str(media_passar) + ' pontos na media' )