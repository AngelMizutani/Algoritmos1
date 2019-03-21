#01. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# numero = int(input('Digite um valor: '))
# if (numero > 0):
#     print('O número informado é POSITIVO!')
# else:
#     print('O número informado é NEGATIVO!')

#2. Faça um Programa que peça dois números e imprima o maior deles.
# num1 = int(input('Digite um valor: '))
# num2 = int(input('Digite outro valor: '))
# if (num1 > num2):
#     print('O número ', num1, ' é o maior número entre eles.')
# else:
#     print('O número ', num2, ' é o maior número entre eles.')

#3. Faça um programa que peça um valor e informe na tela se o número é par ou ímpar.
# numero = int(input('Digite um valor: '))
# if ((numero % 2) == 0):
#     print('O número {} é par'.format(numero))
# else:
#     print('O número {} é ímpar'.format(numero))

#4. Faça um Programa que peça um número e informe se este número é múltiplo de 3.
# numero = int(input('Digite um valor: '))
# if(numero % 3 == 0):
#     print('O número {} é divisível por 3.'.format(numero))
# else:
#     print('O número {} NÃO é divisível por 3.'.format(numero))

#5. Faça um programa que peça dois números e informe se o
 # primeiro é múltiplo do segundo.
# num1 = int(input('Digite um número: '))
# num2 = int(input('Digite outro número: '))
# if (num1 % num2 == 0):
#     print('O número {} é múltiplo de {}.'.format(num1, num2))
# else:
#     print('O número {} NÃO é múltiplo de {}.'.format(num1, num2))

#6. Faça um Programa que verifique o sexo de uma pessoa.
# O usuário deve informar ‘F’ ou ‘M’ e o programa deve escrever
# “Feminino” ou “Masculino”, conforme a letra digitada.
# sexo = input('Informe seu sexo: "F" ou "M": ').upper()
# if(sexo == 'F'):
#     print('Você é do sexo FEMININO')
# else:
#     print('Você é do sexo MASCULINO')

#7. Faça um algoritmo que leia os valores A, B, C
# e imprima na tela se a soma de A + B é maior que C.
# a = int(input('Informe o valor A: '))
# b = int(input('Informe o valor B: '))
# c = int(input('Informe o valor C: '))
# if ((a + b) > c):
#     print('A soma entre A e B é maior que C')
# else:
#     print('A soma entre A e B é menor que C')

#8 Faça um algoritmo que peça um número e se ele for par some 5, se não, some 8.
# num = int(input('Digite um número: '))
# if (num % 2 == 0):
#     soma5 = num + 5
#     print('O número digitado é par, portanto foi somado a 5, resultando em {}'.
#     format(soma5))
# else:
#     soma8 = num + 8
#     print('O número digitado é ímpar, portanto foi somado a 8, resultando em {}'.
#     format(soma8))

#9. Crie um programa que peça uma nota de trabalho e uma de prova (as duas de 0 a 100).
# Se a média aritmética das notas for maior ou igual a 60,
# escreva “Aprovado”, se não, “Reprovado”.
# notaTrab = int(input('Digite a nota do trabalho (0 a 100): '))
# notaProva = int(input('Digite a nota da prova (0 a 100): '))
# media = (notaTrab + notaProva) / 2
# if(media >= 60):
#     print('Aprovado')
# else:
#     print('Reprovado')

# 10. Construa um programa que recebe três valores, A, B e C.
# Em seguida, apresente na tela somente o maior deles.
# a = int(input('Digite o valor de A: '))
# b = int(input('Digite o valor de B: '))
# c = int(input('Digite o valor de C: '))
# if (a > b):
#     if (a > c):
#         print('O número {} é o maior número'.format(a))
#     else:
#         print('O número {} é o maior número'.format(c))
# else:
#     if (b > c):
#         print('O número {} é o maior número'.format(b))
#     else:
#         print('O número {} é o maior número'.format(c))

# a = int(input('Digite o valor de A: '))
# b = int(input('Digite o valor de B: '))
# c = int(input('Digite o valor de C: '))
#
# if (a > b and a > c):
#     print('O número {} é o maior número'.format(a))
#
# elif (a > b and a < c):
#     print('O número {} é o maior número'.format(c))
#
# elif (b > a and b > c):
#     print('O número {} é o maior número'.format(b))
#
# elif (c > a and c > b):
#     print('O número {} é o maior número'.format(b))



#11. Construa um programa que recebe três valores, A, B e C.
# Em seguida, apresente na tela os números em ordem crescente.
# a = int(input('Digite o valor de A: '))
# b = int(input('Digite o valor de B: '))
# c = int(input('Digite o valor de C: '))
# if (a < b):
#     if (a < c):
#         if(b < c):
#             print(a, ', ', b, ', ', c)
#         else:
#             print(a, ', ', c, ', ', b)
#     else:
#         print(c, ', ', a, ', ', b)
# else:
#     if (b < c):
#         if (c < a):
#             print(b, ', ', c, ', ', a)
#         else:
#             print(b, ', ', a, ', ', c)
#     else:
#         print(c, ', ', b, ', ', a)
# a = int(input('Digite o valor de A: '))
# b = int(input('Digite o valor de B: '))
# c = int(input('Digite o valor de C: '))
#
# if (a < b and a < c and b < c):
#     print(a, ',', b, ',', c)
#
# elif (a < b and a < c and c < b):
#     print(a, ',', c, ',', b)
#
# elif (b < a and b < c and a < c):
#     print(b, ',', a, ',', c)
#
# elif (b < a and b < c and c < a):
#     print(b, ',', c, ',', a)
#
# elif (c < a and c < b and a < b):
#     print(c, ',', a, ',', b)
#
# elif (c < a and c < b and b < a):
#     print(c, ',', b, ',', a)


#12. Faça um programa que peça para o usuário digitar um número inteiro.
# Se esse número for negativo, peça para ele digitar um número novamente.
# Por fim, independente do valor, multiplique o número por 10 e
# informe o resultado na tela.
# num = int(input('Digite um número inteiro: '))
# if (num < 0):
#     num = int(input('Digite outro número inteiro: '))
# resultado = num * 10
# print('O resultado do número informado multiplicado por 10 é ', resultado)

#13. Faça um programa para pedir um número inteiro.
# Se esse número for positivo, verifique e informe se ele é par ou ímpar.
# Se ele for negativo, calcule e mostre a diferença entre ele e 100.
# num = int(input('Digite um número inteiro: '))
# if (num > 0):
#     if(num % 2 == 0):
#         print('O número {} é par'.format(num))
#     else:
#         print('O número {} é ímpar'.format(num))
# else:
#     dif = (num + 100)
#     print('A diferença entre {} e 100 é {}'.format(num, dif))


#14. Construa um programa que recebe três valores, A, B e C.
# Em seguida, apresente na tela somente o maior deles.
# Por fim, verifique e informe na tela se esse número é par ou ímpar.
# a = int(input('Digite o valor de A: '))
# b = int(input('Digite o valor de B: '))
# c = int(input('Digite o valor de C: '))
# if (a > b):
#     if (a > c):
#         maiorValor = a
#     else:
#         maiorValor = c
# else:
#     if (b > c):
#         maiorValor = b
#     else:
#         maiorValor = c
# if (maiorValor % 2 == 0):
#     print('O maior valor é {} e esse valor é par.'.format(maiorValor))
# else:
#     print('O maior valor é {} e esse valor é ímpar.'.format(maiorValor))

#15. Uma loja está com uma promoção de 10% desconto em compras acima de R$100.
# Faça um programa que receba um valor, calcule e imprima o
# valor do desconto, se existir, e o valor final da compra.
# valor = float(input('Digite o valor da compra: R$ '))
# if (valor > 100):
#     desconto = valor * 0.1
#     valorFinal = valor - desconto
#     print('Desconto: R$ {} \n Valor Final: R${}'.format(desconto, valorFinal))
# else:
#     valorFinal = valor
#     print('Valor Final: R$ ', valorFinal)

#16. Faça um programa que calcule o valor de imposto a ser pago
# a partir de um salário bruto. Se o salário for maior que R$3.000,00
# deverá ser cobrado 15% de imposto e se for menor, 7,5%.
# Por fim, apresente na tela o salário bruto (total),
# o valor do imposto e o salário líquido (bruto menos o imposto).
# salBruto = float(input('Informe o valor do salário bruto: R$ '))
# if (salBruto > 3000):
#     imposto = salBruto * 0.15
#     salLiq = salBruto - imposto
# else:
#     imposto = salBruto * 0.075
#     salLiq = salBruto - imposto
# print('Salário Bruto = R${}\nImposto = {}\nSalário Líquido = {}'
# .format(salBruto, imposto, salLiq))


#17. Construa um programa para receber 4 números e no final
# apresentar o maior e o menor.
# a = int(input('Digite o valor de A: '))
# b = int(input('Digite o valor de B: '))
# c = int(input('Digite o valor de C: '))
# d = int(input('Digite o valor de D: '))
# if (a > b):
#     if (a > c):
#         if (a > d):
#             maior = a
#         else:
#             maior = d
#     else:
#         if (c > d):
#             maior = c
#         else:
#             maior = d
# else:
#     if (b > c):
#         if (b > d):
#             maior = b
#         else:
#             maior = d
#     else:
#         if (c > d):
#             maior = c
#         else:
#             maior = d
#
# if (a < b):
#     if (a < c):
#         if (a < d):
#             menor = a
#         else:
#             menor = d
#     else:
#         if (c < d):
#             menor = c
#         else:
#             menor = d
# else:
#     if (b < c):
#         if (b < d):
#             menor = b
#         else:
#             menor = d
#     else:
#         if (c < d):
#             menor = c
#         else:
#             menor = d
# print('O maior valor é {}, e o menor valor é {}'.format(maior, menor))

#18. Faça um Programa receba o valor de x, calcule e imprima o valor de f(x)
# que será:
# 	f(x)= 12−x 	se x<2
# f(x)= 1x−2 	se x≥2
# x = int(input('Digite o valor de x: '))
# if (x < 2):
#     fx = 1 / (2 - x)
# else:
#     fx = 1 / (x - 2)
# print('O valor de f(x) é {}'.format(fx))
