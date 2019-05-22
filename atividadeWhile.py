'''
1. Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o
usuário informe um valor válido.
nota = -1
while (nota < 0 or nota > 10):
    nota = int(input('Digite uma nota entre zero e dez: '))
print(nota)

2. Faça um programa que leia um nome de usuário e a sua senha e não aceite
a senha igual ao nome do usuário, mostrando uma mensagem de erro e
voltando a pedir as informações.
nome = ''
senha = ''
while (nome == senha):
    nome = input('Digite o nome: ')
    senha = input('Digite a senha: ')
    if (nome == senha):
        print('A senha deve ser diferente do nome!')
print('Nome: ', nome)
print('Senha: ', senha)

3.Faça um programa que leia e valide as seguintes informações:
    a) Nome: maior que 3 caracteres;
nome = ''
while (len(nome) <= 3):
    nome = input('Digite um nome: ')
    if (len(nome) <= 3):
        print('Nome inválido!')
print('Nome: ', nome)
    b) Idade: entre 0 e 150;
idade = -1
while (idade < 0 or idade > 150):
    idade = int(input('Digite a idade: '))
    if(idade < 0 or idade > 150):
        print('Idade inválida!')
print('Idade: ', idade)

    c) Salário: maior que zero;
salario = 0
while (salario <= 0):
    salario = float(input('Digite o salário: '))
    if (salario <= 0):
        print('Salário inválido!')
print('Salário: ', salario)

    d) Sexo: 'f' ou 'm';
sexo = input('Digite o sexo: ')
if (sexo != 'f' or sexo != 'm'):
    print('Sexo inválido!')
    while (sexo != 'f' or sexo )

sexo = ''
while (sexo != 'F' and sexo != 'M'):
    sexo = (input('Digite o sexo: ')).upper()
    print('s: ', sexo)
    if (sexo != 'F' and sexo != 'M'):
        print(sexo)
        print('Dado inválido!')
print('Sexo: ', sexo)

    e) Estado Civil: 's', 'c', 'v', 'd';
estCiv = ''
while (estCiv != 's' and estCiv != 'c' and estCiv != 'v' and estCiv != 'd'):
    estCiv = input('Digite o estado civil: ')
    if (estCiv != 's' and estCiv != 'c' and estCiv != 'v' and estCiv != 'd'):
        print('Estado Civil Inválido!')

print('Estado civil: ', estCiv)


4. Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para
que a população do país A ultrapasse ou iguale a população do país B,
mantidas as taxas de crescimento.
5. Altere o programa anterior permitindo ao usuário informar as populações
e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo
do outro. Depois modifique o programa para que ele mostre os números
um ao lado do outro.
print('Um embaixo do outro:')
num = 1
while (num <= 20):
    print(num)
    num += 1
print('Um do lado do outro:')
num = 1
while (num <= 20):
    print(num, end = ', ')
    num += 1

7. Faça um programa que leia 5 números e informe o maior número.
maior = 0
cont = 0
while (cont < 5):
    num = int(input('Digite um número: '))

    if (cont == 0):
        maior = num
    else:
        if (num > maior):
            maior = num

    cont += 1

print('O maior número informado é ', maior)

8. Faça um programa que leia 5 números e informe a soma e a média dos números.
cont = 1
soma = 0
while (cont <= 5):
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
media = soma / 5
print('A soma dos números é {} e a média é {}'.format(soma, media))

9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
cont = 1
while (cont <= 50):
    if(cont % 2 != 0):
        print(cont)
    cont += 1

10. Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if (num1 < num2):
    cont = num1
    while(cont <= num2):
        print(cont)
        cont += 1

elif (num2 < num1):
    cont = num2
    while (cont <= num1):
        print(cont)
        cont += 1

else:
    print('Números inválidos!')

11.Altere o programa anterior para mostrar no final a soma dos números.
num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
soma = 0

if (num1 < num2):
    cont = num1
    while(cont <= num2):
        print(cont)
        soma += cont
        cont += 1
    print('A soma dos números é ', soma)

elif (num2 < num1):
    cont = num2
    while (cont <= num1):
        print(cont)
        soma += cont
        cont += 1
    print('A soma dos números é ', soma)

else:
    print('Números inválidos!')


12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
num = int(input('Digite um número inteiro entre 0 e 10: '))
cont = 1
while (cont <= 10):
    print(num, ' X ', cont, ' = ', num * cont)
    cont += 1

13. Faça um programa que peça dois números, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função de potência
da linguagem.
base = int(input('Digite a base: '))
exp = int(input('Digite o expoente: '))
print(base, ' ** ', exp, ' = ', base ** exp)

14. Faça um programa que peça 10 números inteiros, calcule e mostre a
quantidade de números pares e a quantidade de números impares.
cont = 1
qtdePares = 0
qtdeImpares = 0

while (cont <= 10):
    num = int(input('Digite um número inteiro: '))
    if (num % 2 == 0):
        qtdePares += 1
    else:
        qtdeImpares += 1

    cont += 1

print('Quantidade de pares: ', qtdePares)
print('Quantidade de ímpares: ', qtdeImpares)

15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo.
n = int(input('Digite o último termo: '))
termo1 = 0
termo2 = 1
cont = 3
print('{}, {}'.format(termo1, termo2), end = '')

while (cont <= n):
    termo3 = termo1 + termo2
    print(', {}'.format(termo3), end = '')
    termo1 = termo2
    termo2 = termo3
    cont += 1

16. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
termo1 = 0
termo2 = 1
termo3 = termo1 + termo2
cont = 3
print(termo1, ', ', termo2, end = '')

while (termo3 <= 500):
    termo3 = termo1 + termo2
    if (termo3 > 500):
        break
    print(', ', termo3, end = '')
    termo1 = termo2
    termo2 = termo3
    cont += 1

17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''
n = int(input('Digite um número inteiro: '))
fat = 1
print('{}!='.format(n), end = '')
while(n >= 1):
    if (n == 1):
        print('{}'.format(n), end = '')
    else:
        print('{}.'.format(n), end = '')
    fat = fat * n
    n -= 1
print('={}'.format(fat))


'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
Faça um programa que calcule o mostre a média aritmética de N notas.
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
'''
