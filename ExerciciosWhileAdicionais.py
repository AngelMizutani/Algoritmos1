'''
1) Apenas analisando o algoritmo e executando o “teste de mesa”, descreva (sem implementar o código) o
que será executado.
print("comeco do algoritmo") --> será exibida a mensagem na tela
while(True):
    print("dentro do while") --> esse comando será executado infinitamente, pois o valor da condição em while
                                 será sempre True
print("fim do algoritmo") --> esse comando nunca será executado, pois está fora do laço de repetição, e como
                              a repetição será infinita, o sistema nunca vai chegar até essa linha


2) Apenas analisando o algoritmo e executando o “teste de mesa” (sem implementar o código), o que será
exibido ao usuário?
print("comeco do algoritmo") --> essa mensagem será exibida uma vez, ao iniciar a execução do algoritmo
x = 0
while(x < 10):
    print("dentro do while") --> essa mensagem se repetirá infinitas vezes, já que não há alteração no valor
                                 de x na condição do while (a condição sempre será verdadeira)
print("fim do algoritmo") --> essa mensagem nunca será exibida, pois está fora do laço de repetição, que nunca
                              irá acabar.


3) Apenas analisando o algoritmo e executando o “teste de mesa” (sem implementar o código), o que será
exibido ao usuário?
print("comeco do algoritmo") --> essa mensagem será exibida no início do programa
x = 0
while(x < 10):
    print("dentro do while") --> essa mensagem será exibida 10 vezes, já que o valor de x aumenta 1 a cada
                                 repetição
    x = x + 1 --> a cada repetição, o valor de x aumenta 1, até o momento em que a condição do while se torna falsa
print("fim do algoritmo") --> essa mensagem será exibida após o fim da repetição


4) Implemente um algoritmo que seja capaz de solicitar por 4 notas de um aluno. Calcule a média destas
notas e apresente-a ao usuário. Para a resolução, utilize o comando while para a leitura das 4 notas.
cont = 0
soma = 0
while (cont < 4):
    nota = float(input('Digite a nota do aluno: '))
    soma += nota
    cont += 1
print('A média do aluno é ', soma / 4)

5) Faça um algoritmo que seja capaz de solicitar ao usuário por 2 números, não permitindo que números
negativos sejam fornecidos. Em seguida, calcule e apresente:
a) A soma de todos os números no intervalo fornecido pelos dois números
num1 = int(input('Digite um número positivo: '))
num2 = int(input('Digite outro número positivo: '))
if(num1 < 0 or num2 < 0):
    print('Números inválidos!')
else:
    soma = 0
    if (num1 < num2):
        cont = num1
        while(cont <= num2):
            soma += cont
            cont += 1
        print('A soma de todos os números no intervalo entre {} e {} é {}'.format(num1, num2, soma))
    elif (num1 > num2):
        cont = num2
        while (cont <= num1):
            soma += cont
            cont += 1
        print('A soma de todos os números no intervalo entre {} e {} é {}'.format(num2, num1, soma))
    else:
        print('Números inválidos!')


b) A soma de todos os números ímpares no intervalo fornecido pelos dois números
num1 = int(input('Digite um número positivo: '))
num2 = int(input('Digite outro número positivo: '))
if(num1 < 0 or num2 < 0):
    print('Números inválidos!')
else:
    soma = 0
    if (num1 < num2):
        cont = num1
        while(cont <= num2):
            if (cont % 2 != 0):
                soma += cont
            cont += 1
        print('A soma de todos os números ímpares no intervalo entre {} e {} é {}'.format(num1, num2, soma))
    elif (num1 > num2):
        cont = num2
        while (cont <= num1):
            if (cont % 2 != 0):
                soma += cont
            cont += 1
        print('A soma de todos os números ímpares no intervalo entre {} e {} é {}'.format(num2, num1, soma))
    else:
        print('Números inválidos!')


c) Todos os números pares do intervalo fornecido
num1 = int(input('Digite um número positivo: '))
num2 = int(input('Digite outro número positivo: '))
if(num1 < 0 or num2 < 0):
    print('Números inválidos!')
else:
    soma = 0
    if (num1 < num2):
        cont = num1
        while(cont <= num2):
            if (cont % 2 == 0):
                soma += cont
            cont += 1
        print('A soma de todos os números pares no intervalo entre {} e {} é {}'.format(num1, num2, soma))
    elif (num1 > num2):
        cont = num2
        while (cont <= num1):
            if (cont % 2 == 0):
                soma += cont
            cont += 1
        print('A soma de todos os números pares no intervalo entre {} e {} é {}'.format(num2, num1, soma))
    else:
        print('Números inválidos!')

6) Faça um algoritmo que solicite ao usuário por um número inteiro. Apresente ao usuário a tabuada (de 1 a
10) do valor lido.
num = int(input('Digite um número inteiro: '))
cont = 1
while (cont <= 10):
    print('{} * {} = {}'.format(num, cont, num*cont))
    cont += 1

7) No Python 3.x, cada comando print() é exibido em uma linha, ou seja, existe um “\n” ao final da
apresentação do conteúdo na tela. Para que não haja quebra de linha e os comandos print() sejam exibidos
na mesma linha, podemos utilizar vários comandos print("mensagem", end=""). Neste sentido, implemente
um algoritmo que, com apenas um comando print(“*”, end=“”) apresente os seguintes padrões na tela (caso
seja necessário a quebra de linha, utilize print()):
a)
*********
********
*******
******
*****
****
***
**
*
linha = 0
qtde = 9
while (linha < 9):
    cont = 0
    while(cont < qtde):
        print('*', end = '')
        cont += 1
    print()
    qtde -= 1
    linha += 1

b)
*
**
***
****
*****
******
*******
********
*********
**********
linha = 0
qtde = 1
while (linha < 9):
    cont = 0
    while(cont < qtde):
        print('*', end = '')
        cont += 1
    print()
    qtde += 1
    linha += 1

8) Um fatorial é calculado da seguinte maneira: 4! = 4 * 3 * 2 * 1 = 24. Temos que 0! = 1. Não calculamos
fatorial de valores negativos. Implemente um algoritmo que seja capaz de solicitar um número inteiro
positivo ao usuário, limitando-o no intervalo de 0 a 10. Calcule e apresente o fatorial deste número.
num = int(input('Digite um número inteiro positivo de 0 a 10: '))
if (num < 0 or num > 10):
    print('Número inválido!')

else:
    if (num == 0):
        print('0! = 1')

    else:
        cont = num
        fatorial = 1
        while (cont >= 1):
            fatorial = fatorial * cont
            cont -= 1
        print('{}! = {}'.format(num, fatorial))

9) Um algoritmo representado em Fluxograma é apresentado abaixo. Codifique-o utilizando a linguagem
Python. O que será exibido ao executar o algoritmo?
e = int(input('Digite um valor: '))
s = 0
l = 0
t = 1

while (t >= e):
    s = s + t
    l = l + 2
    t = 1 / l
print(s)

10) Faça um algoritmo que verifique e mostre todos os números entre 1000 e 2000 (inclusive) que, quando
divididos por 11, produzam resto igual a 5.
cont = 1000
while (cont <= 2000):
    if (cont % 11 == 5):
        print(cont)
    cont += 1

11) Faça um programa que leia um valor inteiro n positivo, calcule e mostre a seguinte soma:
n = int(input('Digite um número inteiro positivo: '))
if (n <= 0):
    print('Número inválido!')

else:
    soma = 0
    cont = 1
    while (cont <= n):
        soma = soma + (1/cont)
        cont += 1
    print(soma)

12) Uma loja possui 15 clientes cadastrados e deseja enviar uma correspondência a cada um deles
anunciando um bônus especial. Faça um programa que leia o nome de cada cliente e o valor total de suas
compras no ano passado. Calcule e mostre um bônus de 10% se o valor da compra for menor que R$ 1000,00
e de 15%, caso contrário.
cont = 0
while (cont <= 15):
    nome = input('Nome do Cliente: ')
    valorCompras = float(input('Valor total das compras: R$ '))

    if (valorCompras > 0 and valorCompras < 1000):
        bonus = '10%'
    else:
        bonus = '15%'

    print('Olá {}! Você acaba de receber um bônus especial de {}!\n'.format(nome, bonus))
    cont += 1

13) Faça um programa que faça a leitura da idade de 40 pessoas. Calcule e mostre quantas pessoas possuem
mais de 30 anos.
cont = 0
maisDe30 = 0
while (cont < 40):
    idade = int(input('Idade: '))
    if (idade > 30):
        maisDe30 += 1
    cont += 1
print('{} pessoas possuem mais de 30 anos.'.format(maisDe30))

14) Uma loja atendeu na última hora 10 clientes. Um sistema informatizado precisa armazenar o valor pago
por cada cliente e também um código para o tipo de pagamento efetuado, sendo ‘V’ para pagamento a vista
e ‘P’ para pagamento a prazo. Desenvolva um sistema que solicite, para os 10 clientes, os valores de suas
compras e o código do tipo de pagamento. Em seguida, calcule e mostre:
a) O valor total das vendas a vista
cont = 1
total = 0
while (cont <= 10):
    valor = float(input('Valor Pago: R$ '))
    tipoPagamento = (input('Tipo de Pagamento: ')).upper()
    print('------------------------')

    if (tipoPagamento == 'V'):
        total += valor

    cont += 1
print('Valor total das vendas a vista: R$ ', total)

b) O valor total das vendas a prazo
cont = 1
total = 0
while (cont <= 10):
    valor = float(input('Valor Pago: R$ '))
    tipoPagamento = (input('Tipo de Pagamento: ')).upper()
    print('------------------------')

    if (tipoPagamento == 'P'):
        total += valor

    cont += 1
print('Valor total das vendas a prazo: R$ ', total)

c) O valor total das vendas efetuadas
cont = 1
total = 0
while (cont <= 10):
    valor = float(input('Valor Pago: R$ '))
    total += valor

    cont += 1
print('Valor total das vendas: R$ ', total)

15) Faça um programa que leia a idade, a altura e o peso de 15 pessoas. Calcule e mostre:
a) A quantidade de pessoas com idade igual ou superior a 50 anos
cont = 1
qtde = 0
while (cont <= 15):
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))
    print('------------------------')
    if(idade >= 50):
        qtde += 1
    cont += 1
print('A quantidade de pessoas com 50 anos ou mais é ', qtde)

b) A média das alturas de todas as pessoas
cont = 1
somaAlturas = 0
while (cont <= 15):
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))
    print('------------------------')

    somaAlturas += altura

    cont += 1
print('A média das alturas das pessoas é ', somaAlturas/15)

c) A média das alturas de todas as pessoas que possuem entre 10 e 20 anos
cont = 1
somaAlturas = 0
qtde = 0
while (cont <= 15):
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))
    print('------------------------')

    if (idade >= 10 and idade <= 20):
        somaAlturas += altura
        qtde += 1

    cont += 1
print('A média das alturas das pessoas enre 10 e 20 anos é ', somaAlturas/qtde)

d) A porcentagem de pessoas com peso inferior a 60Kg entre todas as pessoas analisadas
cont = 1
qtde = 0
while (cont <= 15):
    idade = int(input('Idade: '))
    altura = float(input('Altura: '))
    peso = float(input('Peso: '))
    print('------------------------')

    if (peso < 60):
        qtde += 1

    cont += 1
porcentagem = (qtde / 15) * 100
print('A porcentagem de pessoas com peso inferior a 60 kg é ', porcentagem)

16) Foi feita uma pesquisa entre os habitantes de uma cidade. Foram coletados os dados da idade, sexo (M/F)
e salário. Desenvolva um programa que calcule e mostre:
a) A média dos salários dos habitantes
hab = 0
idade = 0
somaSalario = 0
while (idade >= 0):
    idade = int(input('Idade: '))
    if (idade >= 0):
        sexo = (input('Sexo: ')).upper()
        salario = float(input('Salário: '))
        somaSalario += salario
        hab += 1
print('A média de salário dos habitantes é ', somaSalario / hab)

b) A maior e a menor idade informada
hab = 0
idade = 0
maiorIdade = 0
menorIdade = 0
while (idade >= 0):
    idade = int(input('Idade: '))
    if (idade >= 0):
        sexo = (input('Sexo: ')).upper()
        salario = float(input('Salário: '))

        if (hab == 0):
            maiorIdade = idade
            menorIdade = idade
        else:
            if (idade > maiorIdade):
                maiorIdade = idade
            elif (idade < menorIdade):
                menorIdade = idade
        hab += 1
print('A maior idade é {} e a menor idade é {}'.format(maiorIdade, menorIdade))

c) A quantidade de mulheres que recebem salários até R$ 2500,00
hab = 0
idade = 0
qtde = 0
while (idade >= 0):
    idade = int(input('Idade: '))
    if (idade >= 0):
        sexo = (input('Sexo: ')).upper()
        salario = float(input('Salário: R$ '))
        if (sexo == 'F' and salario < 2500):
            qtde += 1
    hab += 1

print('A quantidade de mulheres com salários até R$ 2500,00 é ', qtde)

d) A idade e o sexo da pessoa que possui o menor salário
O programa deve ser finalizado quando a idade informada for um valor negativo.
hab = 0
idade = 0
qtde = 0
menorSalario = 0
while (idade >= 0):
    idade = int(input('Idade: '))
    if (idade >= 0):
        sexo = (input('Sexo: ')).upper()
        salario = float(input('Salário: R$ '))

        if (hab == 0):
            menorSalario = salario
        else:
            if (salario < menorSalario):
                sMenor = sexo
                iMenor = idade

    hab += 1

print('A pessoa com menor salário é do sexo {} e tem {} anos'.format(sMenor, iMenor))

17) Faça um programa que apresente o seguinte menu ao usuário:
Menu de opções:
1. Média aritmética
2. Média ponderada
3. Exibir mensagem de boas vindas
4. Sair
Digite a opção desejada: __
Ao escolher a opção 1, o usuário deve informar duas notas e apresentar a média destas notas.
Ao escolher a opção 2, o usuário deve informar três notas e seus respectivos pesos, calcular e apresentar a
média ponderada.
Ao escolher a opção 3, uma mensagem de boas vindas deverá ser exibida ao usuário.
Ao escolher a opção 4, o sistema deve ser finalizado.
Ao escolher uma opção inválida, o sistema deverá informar ao usuário que esta opção é inválida.
A cada escolha da opção, o sistema deve executar o que se pede e retornar ao menu de opções, sendo
finalizado apenas quando o usuário informar 4.
opcao = 0
while (opcao != 4):
    print('=========================\n' +
    'Menu de opções: \n' +
    '1. Média aritmética \n' +
    '2. Média ponderada \n' +
    '3. Exibir mensagem de boas vindas \n' +
    '4. Sair')
    opcao = int(input('Digite a opção desejada: '))

    if (opcao == 1):
        nota1 = float(input('Digite uma nota: '))
        nota2 = float(input('Digite outra nota: '))
        print('A média das notas é ', (nota1 + nota2)/2)

    elif (opcao == 2):
        nota1 = float(input('Digite uma nota: '))
        peso1 = int(input('Digite o peso: '))
        nota2 = float(input('Digite outra nota: '))
        peso2 = int(input('Digite o peso: '))
        nota3 = float(input('Digite outra nota: '))
        peso3 = int(input('Digite o peso: '))
        media = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)
        print('A média ponderada das notas é ', media)

    elif (opcao == 3):
        print('Bem-Vindo!!!!!!!')

    elif (opcao == 4):
        break

    else:
        print('Opção inválida!!')

18) Crie um programa que apresente o seguinte menu ao usuário:
Opções disponíveis:
1. Exibir os quadrados de 5 números
2. Exibir números pares em um intervalo informado
3. Exibir o caractere * em uma diagonal de 10 linhas
4. Exibir os números de 10 a 1
5. Exibir a raiz quadrada de 4 números informados pelo usuário
6. Exibir o valor de bn, onde b e n devem ser solicitados ao usuário
7. Sair
Digite sua opção: ____
Ao escolher (1), o sistema deve solicitar por 5 números e exibir o quadrado de cada número informado. Na
opção (2), o sistema deverá solicitar dois números e apresentar todos os números pares entre os dois
números informados. Na opção (3), deverá ser exibida uma diagonal contendo 10 linhas:
*
 *
  *
   *
    *
     *
      *
       *
        *
         *
Ao escolher (4), o sistema deverá exibir os números de 10 a 1. Na opção (5), o sistema deve solicitar 4
números ao usuário e apresentar a raiz quadrada de cada número. Na opção (6), o usuário informará dois
valores: a base e o expoente, o sistema deverá exibir a base elevado ao expoente. Caso o usuário informe um
valor diferente de 1~7, o sistema deverá emitir uma mensagem de erro. O sistema só será finalizado ao
digitar a opção 7. A cada execução da opção escolhida, o sistema deve retornar ao menu principal.
'''
opcao = 0
while (opcao != 7):
    print('\n=================================\n' +
    'Opções disponíveis:\n' +
    '1. Exibir os quadrados de 5 números\n' +
    '2. Exibir números pares em um intervalo informado\n' +
    '3. Exibir o caractere * em uma diagonal de 10 linhas\n' +
    '4. Exibir os números de 10 a 1\n' +
    '5. Exibir a raiz quadrada de 4 números informados pelo usuário\n' +
    '6. Exibir o valor de bn, onde b e n devem ser solicitados ao usuário\n'+
    '7. Sair')
    opcao = int(input('Digite sua opção: '))

    if (opcao == 1):
        cont = 0
        while(cont < 5):
            num = int(input('Digite um número: '))
            print('O quadrado do número é ', num ** 2)
            cont += 1

    elif (opcao == 2):
        x = int(input('Digite um número: '))
        y = int(input('Digite outro número: '))
        cont = 0

        if (x < y):
            cont = x
            while (cont <= y):
                if (cont % 2 == 0):
                    print(cont)
                cont += 1

        elif (x > y):
            cont = y
            while (cont <= x):
                if (cont % 2 == 0):
                    print(cont)
                cont += 1

        else:
            print('Valores inválidos!')

    elif (opcao == 3):
        linhas = 0
        espacos = 0
        while (linhas < 9):
            cont = 0
            while (cont < espacos):
                print(' ', end='')
                cont += 1
            print('*')
            espacos += 1
            linhas += 1

    elif (opcao == 4):
        cont = 10
        while (cont > 0):
            print(cont)
            cont -= 1

    elif (opcao == 5):
        cont = 0
        while (cont < 4):
            num = int(input('Digite um número: '))
            print('A raiz quadrada desse número é ', num ** (1/2))
            cont += 1

    elif (opcao == 6):
        num = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
        print('O número {} elevado a {} é igual a {}'.format(num, num2, (num ** num2)))


    elif (opcao == 7):
        break

'''
19) Crie um algoritmo que solicite um limite inferior e um limite superior. Garanta que o limite superior seja
um valor válido. Solicite também um valor de incremento. O sistema deverá apresentar na tela todos os
números do limite inferior ao limite superior, respeitando o valor de incremento. Exemplo:
Limite inferior: 0
Limite superior: 47
Incremento: 5
0 5 10 15 20 25 30 35 40 45
20) Para converter graus Célsius em Fahrenheit, utilizamos a fórmula � = .(0123)
5
.
Elabore um programa que solicite uma temperatura inicial e final em Fahrenheit, e também solicite um valor
de incremento. Exiba ao usuário uma tabela contendo a conversão dos graus entre as temperaturas inicial e
final, incrementando conforme o valor informado. Por exemplo:
Temperatura inicial: 50
Temperatura final: 150
Incremento: 4
Fahrenheit Celcius
50 10
54 12.22
58 14.44
62 16.66
...
150 65.55
21) Crie um algoritmo que solicite ao usuário por um número que representa quantos valores serão
fornecidos ao programa. Em seguida, leia os n números e apresente, para cada número, o seu triplo. Exemplo:
Quantos números: 3
Número: 8 Triplo: 24
Número: 10 Triplo: 30
Número: 1 Triplo: 3
'''
