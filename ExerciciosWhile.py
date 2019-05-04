'''
1. Faça algoritmos em Python, utilizando o ​while​,​ ​que:
a) Apresente na tela os números de 1 a 100.

x = 1
while (x <= 100):
    print(x)
    x = x + 1


b) Faça a soma dos números de 1 a 100 e apresente somente o 
resultado.

x = 1
soma = 0
while (x <= 100):
    soma = soma + x
    x = x + 1
    print(soma)

c) Apresente na tela somente os números pares entre 1 e 100.

cont = 1
while (cont <= 100):
    if (cont % 2 == 0):
        print(cont)
    cont = cont + 1

d) Apresente na tela somente a soma dos números pares entre 1 e 100.

cont = 1
soma = 0
while (cont <= 100):
    if (cont % 2 == 0):
        soma = soma + cont
        print(soma)
    cont = cont + 1

e) Apresente na tela os números de X a Y (peça para o usuário informar os valores de X e
de Y).

x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))

if (x < y):
    while (x <= y):
        print(x)
        x = x + 1
elif (x > y):
    while (y <= x):
        print(y)
        y = y + 1
else:
    print('Valores inválidos!')

f) Faça a soma dos números de X a Y e apresente somente o resultado (peça para o
usuário informar os valores de X e de Y).

soma = 0
x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))

if (x < y):
    while (x <= y):
        soma = soma + x
        print(soma)
        x = x + 1

elif (x > y):
    while ( y <= x):
        soma = soma + y
        print(soma)
        y = y + 1

else:
    print('Valores inválidos!')


g) Apresente na tela somente os números ímpares entre X e Y (peça para o usuário
informar os valores de X e de Y).

x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))

if (x < y):
    while (x <= y):
        if (x % 2 == 1):
            print(x)
        x = x + 1

elif (x > y):
    while (y <= x):
        if (y % 2 == 1):
            print(y)
        y = y + 1

else:
    print('Valores inválidos!')

2.Faça um programa para calcular a tabuada:
a) do 1 ao 10 para um número informado pelo usuário.

x = int(input('Informe um número: '))
cont = 1

while (cont <= 10):
    print(x, ' * ', cont, ' = ', (x * cont))
    cont += 1

b)do X ao Y para um número informado pelo usuário (o usuário também deve informar os valores de X e Y).

x = int(input('Informe o valor de X: '))
y = int(input('Informe o valor de Y: '))

if(x < y):
    cont = x
    while (cont <= y):
        print(x, ' * ', cont, ' = ', x * cont)
        cont += 1

elif (x > y):
    cont = y
    while (cont <= 10):
        print (y, ' * ', cont, ' = ', y * cont)
        cont += 1

else:
    print('Valores inválidos!')


3. Na matemática, o fatorial de um número natural n, representado por n!, é o produto de todos os inteiros positivos
 menores ou iguais a n. Por exemplo: o fatorial de 5 é representado por 5! que é igual a 5 x 4 x 3 x 2 x 1. 
 Faça um programa que peça um número para o usuário e apresente na tela seu fatorial.

num = int(input('Digite um número inteiro: '))
cont = num
fatorial = 1

while (cont >= 1):
    fatorial = fatorial * cont
    cont -= 1
print('O fatorial do número {} é {}'.format(num, fatorial))

4. Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação. 
O programa será executado repetidamente até que o usuário passe o número informado para sair do programa (opção).
====== Menu Principal ======
1. Par ou ímpar?
2. Potência XY
3. Raiz quadrada
4. Sair
Observação: Se o usuário informar uma opção inválida, apresente uma mensagem informando isso.

num = 0
while (num != 4):
    print('
    ====== Menu Principal ======\n
    1. Par ou ímpar?\n
    2. Potência XY\n
    3. Raiz quadrada\n
    4. Sair\n
    ')
    num = int(input('Escolha uma das opções: '))

    if (num == 1):
        x = int(input('Informe um número inteiro: '))
        if (x % 2 == 0):
            print('O número {} é par.'.format(x))
        else:
            print('O número {} é ímpar.'.format(x))
    
    elif (num == 2):
        x = int(input('Informe um número inteiro: '))
        y = int(input('Informe outro número inteiro: '))
        pot = x ** y
        print('O número {} elevado a {} é igual a {}'.format(x, y, pot))

    elif (num == 3):
        x = int(input('Informe um número inteiro positivo: '))
        if(x >= 0):
            raiz = x ** (1/2)
            print('A raiz quadrada de {} é igual a {}'.format(x, raiz))
        elif(x < 0):
            print('Não é possível calcular raiz quadrada de número negativo!')

    elif (num == 4):
        break
    
    else:
        print('Opção inválida! Tente novamente!')

5. Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação. 
O programa será executado repetidamente até que o usuário passe o número informado para sair do programa (opção).
====== Menu Principal ======
1. Fazer a tabuada do 1 ao 10 para um número X
2. Apresentar os múltiplos de X entre 1 e 100
3. Apresentar a soma dos números de 1 a 100
4. Sair do programa

opcao = 0
while (opcao != 4):
    print('====== Menu Principal ======\n' +
    '1. Fazer a tabuada do 1 ao 10 para um número X\n' +
    '2. Apresentar os múltiplos de X entre 1 e 100\n' +
    '3. Apresentar a soma dos números de 1 a 100\n' +
    '4. Sair do programa\n')

    opcao = int(input('Escolha uma opção: '))

    if (opcao == 1):
        x = int(input('Informe um número inteiro: '))
        cont = 1
        while (cont <= 10):
            print(x, ' * ', cont, ' = ', x * cont)
            cont += 1

    elif (opcao == 2):
        x = int(input('Digite um número inteiro: '))
        cont = 1
        while (cont <= 100):
            if(cont % x == 0):
                print(cont)
            cont += 1

    elif (opcao == 3):
        soma = 0
        cont = 1
        while (cont <= 100):
            soma = soma + cont
            cont += 1
        print('A soma dos números de 1 a 100 é igual a ', soma)

    elif (opcao == 4):
        break
    
    else:
        print('Opção inválida! Tente novamente!')

6. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora. O programa deverá receber um número desconhecido de 
valores referentes aos preços das mercadorias. O valor “0” (zero) deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
para então calcular e mostrar o valor do troco. A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 10.00
Produto 4: R$ 0
Total: R$ 18.00
Dinheiro: R$ 20.00
Troco: R$ 2.00

valor = 1
cont = 1
soma = 0

print('Lojas Tabajara')
while (valor != 0):
    valor = float(input('Produto {}: R$ '.format(cont)))
    soma = soma + valor
    # print('Produto {}: R$ {}'.format(cont, valor))
    cont += 1

print('Total: R$ {:.2f}'.format(soma))
dinheiro = float(input('Dinheiro: R$ '))
print('Troco: R$ {:.2f}'.format(dinheiro - soma))
    

7. O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia 
 um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas 
 informadas, bem como a média das temperaturas. 

temp = 1
cont = 0
soma = 0
maior = 0
menor = 1000000
while (temp != 0):
    temp = float(input('Temperatura {}: '.format(cont + 1)))
    if (temp != 0):
        if (temp > maior):
            maior = temp
        elif (temp < menor):
            menor = temp
        soma = soma + temp
        cont += 1
print('Menor Temperatura: ', menor)
print('Maior Temperatura: ', maior)
print('Média das Temperaturas: ', soma, " / ", cont, ' = ', soma / cont)


8. Faça um programa que calcule e mostre a média aritmética de N notas informadas pelo usuário. 
O programa pode parar de pedir notas quando o usuário informar -1, por exemplo. 

nota = 0
cont = 1
soma = 0
while(nota != -1):
    nota = float(input('Nota {}: '.format(cont)))
    if (nota != -1):
        soma += nota
        media = soma / cont
        cont += 1
print('Média: ', media)

9. Faça um programa que calcule o valor total investido por um colecionador 
em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um. 
valor = 0
qtde = 1
soma = 0
while (valor != -1):
    valor = float(input('Valor CD{}: R$ '.format(qtde)))
    if (valor != -1):
        soma = soma + valor
        media = soma / qtde
        qtde += 1
print('Total: R$ {:.2f}'.format(soma))
print('Valor Médio: R$ {:.2f}'.format(media))


10.Uma academia deseja fazer um questionário entre seus clientes para descobrir o mais alto, o mais baixo, 
o mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos 
clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser 
dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser 
informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes 

cod = ''
maisAlto = 0
maisBaixo = 3
maisGordo = 0
maisMagro = 1000
cont = 1
somaAlt = 0
somaPeso = 0
while (cod != '0'):
    cod = input('Informe o seu código: ')
    if (cod != '0'):
        altura = float(input('Informe sua altura: '))
        if (altura >= maisAlto):
            maisAlto = altura
            codMaisAlto = cod
        if (altura <= maisBaixo):
            maisBaixo = altura
            codMaisBaixo = cod
        somaAlt += altura
        mediaAlt = somaAlt / cont

        peso = float(input('Informe o seu peso: '))
        if (peso >= maisGordo):
            maisGordo = peso
            codMaisGordo = cod
        if (peso <= maisMagro):
            maisMagro = peso
            codMaisMagro = cod
        somaPeso += peso
        mediaPeso = somaPeso / cont
        
        cont += 1
print('\nCliente mais alto: ', codMaisAlto)
print('Altura: ', maisAlto)
print('\nCliente mais baixo: ', codMaisBaixo)
print('Altura: ', maisBaixo)
print('\nCliente mais gordo: ', codMaisGordo)
print('Peso: ', maisGordo)
print('\nCliente mais magro: ', codMaisMagro)
print('Peso: ', maisMagro)
print('Média das alturas: ', mediaAlt)
print('Média dos pesos: ', mediaPeso)


11. Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que peça ao usuário qual o termo final (N)
 e calcule o valor de H. 
cont = 1
h = 0
n = int(input('Informe um valor inteiro para N: '))
while (cont <= n):
    h = h + (1 / cont)
    cont += 1
print(h)

12.Em uma competição de ginástica, cada atleta recebe votos de sete jurados. 
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas 
pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). 
As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo: 
Lojas Tabajara 
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9.04

cont = 0
menor = 10
maior = 0
soma = 0
print('Lojas Tabajara')
nome = input('Atleta: ')
while (cont < 7):
    nota = float(input('Nota: '))
    if (nota > maior):
        maior = nota
    if (nota < menor):
        menor = nota
    soma = soma + nota
    cont += 1
media = (soma - maior - menor) / 5
print('\nResultado Final:')
print('Atleta: ', nome)
print('Melhor nota: ', maior)
print('Pior nota: ', menor)
print('Média: ', media)    


13.Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e apresente o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento de cada um.

ano = 0
a = 80000
b = 200000
while (a <= b):
    a = a * 1.03
    b = b * 1.015
    ano += 1
    
    
print('O número de anos para a população A ultrapassar ou igualar a população B é ', ano)


14. Desafio sem usar strings: faça um programa que peça para o usuário informar um número entre 1 e 999. 
Em seguida, apresente esse número invertido.
Digite um número: 481
Número invertido: 184
'''
num = int(input('Digite um número entre 1 e 999: '))
if (num >= 1 and num <= 999):
    unidade = num % 10
    dezena = num % 100 - unidade
    centena = int(num /100)
    numInv = (unidade * 100) + dezena + centena
    print('Número invertido: ', numInv)
else:
    print('Número inválido!')




    