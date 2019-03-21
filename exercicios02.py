#19. Construa um programa que mostre menu exatamente como o exemplo abaixo
 # e implemente as funções necessárias:
# 	== Menu de Opções ==
# 	1. Somar 2 números
# 	2. Potência de um número
# 3. Raiz de grau N
# == Opção escolhida:
# print('== Menu de Opções ==')
# print('1. Somar 2 números')
# print('2. Potência de um número')
# print('3. Raiz de grau N')
# opcao = input('== Opção escolhida: ')
# if (opcao == '1'):
#     print('Opção escolhida: 1')
# elif (opcao == '2'):
#     print('Opção escolhida: 2')
# else:
#     print('Opção escolhida: 3')

#20. Construa um programa para determinar se o indivíduo
# está com um peso favorável.
# Essa situação é determinada através do IMC (Índice de Massa Corporal),
# que é definida como sendo a relação entre o peso e o quadrado
# da altura do indivíduo.
# Ou seja: IMC = peso/altura² e a situação do peso é determinada pela tabela abaixo:
# peso = float(input('Digite o seu peso: '))
# altura = float(input('Digite sua altura: '))
# imc = peso / (altura ** 2)
# if (imc < 18.5):
#     print('Você está com baixo peso!')
# elif (imc < 24.9):
#     print('Parabéns! Você está com peso normal!')
# elif (imc < 29.9):
#     print('Você está na pré-obesidade!')
# elif (imc < 34.9):
#     print('Você tem Obesidade Grau I!')
# elif (imc < 39.9):
#     print('Você tem Obesidade Grau II!')
# else:
#     print('Você tem Obesidade Grau III!')

# 21. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e o contrataram
# para desenvolver o programa que vai calcular os reajustes.
# Faça um programa que recebe o salário de um colaborador e calcule o reajuste segundo o seguinte critério baseado no salário atual:
# - até R$ 710,00 (incluindo): aumento de 20%
# - entre R$ 710,00 e R$ 1.000,00: aumento de 15%
# - entre R$ 1.000,00 e R$ 2.500,00: aumento de 10%
# - de R$ 2.500,00 em diante: aumento de 5%
# Após o aumento ser realizado, informe na tela:
# - salário antes do reajuste;
# - percentual de aumento aplicado;
# - valor do aumento;
# - novo salário, após o aumento.
# salario = float(input('Informe o salário do colaborador: '))
# if (salario <= 710):
#     porcento = '20%'
#     aumento = salario * 0.2
#     salarioNovo = salario + aumento
#
# elif (salario > 710 and salario < 1000):
#     porcento = '15%'
#     aumento = salario * 0.15
#     salarioNovo = salario + aumento
#
# elif (salario >= 1000 and salario < 2500):
#     porcento = '10%'
#     aumento = salario * 0.1
#     salarioNovo = salario + aumento
#
# else:
#     porcento = '5%'
#     aumento = salario * 0.05
#     salarioNovo = salario + aumento
#
# print('''
# SALÁRIO ANTES DO REAJUSTE: R$ {}
# PERCENTUAL DE AUMENTO APLICADO: {}
# VALOR DO AUMENTO: R$ {}
# NOVO SALÁRIO: R$ {}
# '''.format(salario, porcento, aumento, salarioNovo))


#
#22. Uma frutaria está vendendo frutas com a seguinte tabela de preços:
# 			       Até 5 Kg		         Acima de 5 Kg
# Morango   	R$ 8,90 por Kg 	           R$ 7,90 por Kg
# Maçã     	    R$ 3,90 por Kg      	   R$ 3,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
# ultrapassar R$25,00, receberá ainda um desconto de 7% sobre este total.
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg)
 # de maçãs adquiridas e calcule o valor a ser pago pelo cliente.
# qtdeMorango = float(input('Quantidade de morangos: '))
# qtdeMaca = float(input('Quantidade de maçãs: '))
# qtdeTotal = qtdeMorango + qtdeMaca
#
# if (qtdeMorango <= 5):
#     valorMorango = 8.9 * qtdeMorango
# else:
#     valorMorango = 7.9 * qtdeMorango
#
# if (qtdeMaca <= 5):
#     valorMaca = 3.9 * qtdeMaca
# else:
#     valorMaca = 3.5 * qtdeMaca
#
# valorTotal = valorMorango + valorMaca
#
# if (qtdeTotal > 8 or valorTotal > 25):
#     valorTotal *= 0.93
#
# print('Total a pagar: R$ {}'.format(valorTotal))

#23. Faça um Programa para calcular a quantidade de notas de um troco.
# O programa deverá perguntar ao usuário o valor do troco (inteiro) e depois
# informar quantas notas (considere R$1 como nota, pois temos moeda) de cada
# valor serão fornecidas. As notas disponíveis serão as de 1, 2, 5, 10, 50 e 100 reais.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas
# de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de
# 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
troco = int(input('Digite o valor do troco: R$ '))
