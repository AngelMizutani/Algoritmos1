'''
4) Implemente um programa que seja capaz de criar um vetor com os elementos a seguir, e exiba-os na tela do usuário:
    x=[10.9, 8.7, 9.123, -9.8, -2.0, 14523.4, -78451, 0]

x = [10.9, 8.7, 9.123, -9.8, -2.0, 14523.4, -78451, 0]
for i in range (0, len(x)):
    print(x[i])


5) Implemente um programa que seja capaz de criar um vetor com os elementos a seguir, e exiba-os na tela do usuário:
    disciplinas={"Português", "Matemática", "Física", "Química"};
disciplinas = ["Português", "Matemática", "Física", "Química"]
for i in range (0, len(disciplinas)):
    print(disciplinas[i])

7) Um programa de computador deve ser capaz de armazenar o nome de oito pessoas da sua família. 
Implemente um programa que seja capaz de solicitar os nomes(armazenando-os em um vetor) e, após digitar 
todos os nomes, exiba-os ao usuário.
nomes = [''] * 8

for cont in range (0, len(nomes)):
    nomes[cont] = input('Digite o nome: ')

for cont in range (0, len(nomes)):
    print(nomes[cont])

8) Crie um programa que solicite ao usuário pelo preço de 15 produtos. 
Em seguida, apresente ao usuário todos os preços digitados.
precos = [0] * 15

for cont in range (0, len(precos)):
    precos[cont] = float(input('Digite o preço: '))
    
for cont in range (0, len(precos)):
    print('Preço', cont, '=', precos[cont])


9) Um programa de computador deve ser capaz de solicitar ao usuário o nome de 10 cidades e 
também a população de cada uma destas cidades. Implemente um programa que represente esta situação. 
Após informar as 10 cidades com suas respectivas populações, apresente ao usuário os valores informados 
conforme o exemplo abaixo: Cidade - População Paranavaí - 105470 Terra Rica - 15256 Paranacity - 11361 .....
cidades = [''] * 10
populacoes = [0] * 10

for cont in range (0, len(cidades)):
    cidades[cont] = input('Cidade: ')
    populacoes[cont] = int(input('População: '))

print('====================================')
print('Cidade\t\t - População')

for cont in range (0, len(cidades)):
    print(cidades[cont], '\t-', populacoes[cont])


10) Ao criar um vetor(array unidimensional), temos que fornecer o número de elementos deste array. 
O número de elementos deve ser um valor inteiro positivo. Por exemplo:
    x=[0]*50; faz com que um vetor chamado “x” seja criado, e este vetor irá armazenar 50 números inteiros. 
    Como o valor 50 é um número inteiro, este valor pode ser representado por uma variável inteira. Por exemplo:
    tamanho=50; x=[0] * tamanho; Implemente um programa que solicite primeiramente ao usuário por quantos 
    números inteiros ele desejará fornecer ao sistema. Em seguida, solicite ao usuário a quantia de números informados. 
    Por fim, apresente na tela todos os números informados.
tamanho = int(input('Tamanho do vetor: '))
vetor = [0] * tamanho

for cont in range (0, tamanho):
    vetor[cont] = int(input('Digite um valor: '))

for cont in range (0, tamanho):
    print(vetor[cont], end=' ')

11) Faça um programa que solicite ao usuário por uma quantia de números inteiros a ser digitada. 
Em seguida, solicite pelos números ao usuário. Após preencher a lista com os números, o programa 
deverá solicitar ao usuário por um outro valor e exibir uma mensagem informando se este último valor 
está presente ou não na lista.
tamanho = int(input('Quantia de números a ser digitada: '))
vetor = [0] * tamanho

for cont in range (0, tamanho):
    vetor[cont] = int(input('Digite um número: '))

print(vetor)

item = int(input('Digite o item a ser procurado: '))
posicao = -1

for cont in range (0, tamanho):
    if (vetor[cont] == item):
        posicao = cont
        break

if (posicao >= 0):
    print('O valor procurado está na posicao', posicao)

else:
    print('Valor não encontrado!')

12)(Continuação do Exercício 11) Além de exibir se o valor está presente ou não no vetor, 
caso ele esteja presente, informar qual a posição deste valor no vetor.

13) Considere que em um programa existam dois vetores:
    A=[10, 12, 13, 15, 8, 1, 0, 5] B=[8, 3, -1, -2, 5, 15, 0, 1] 
    O programa deve ser capaz de criar o terceiro vetor C e armazenar neste vetor,
     para cada elemento, a soma dos valores de A e B. Por exemplo:
    A 10 12 13 15 8 1 0 5 B 8 3 - 1 - 2 5 15 0 1
    C 18 15 12 13 13 16 0 6 Para que o vetor C seja preenchido, utilize um laço de repetição. 
    DICA: para C[1], temos A[1] + B[1]. Ao final da soma, exiba os valores dos vetores A, B e C.
A = [10, 12, 13, 15, 8, 1, 0, 5]
B = [8, 3, -1, -2, 5, 15, 0, 1]
C = [0] * 8

for cont in range (0, len(A)):
    C[cont] = A[cont] + B[cont]

print('A = [', end='')
for cont in range (0, len(A)):
    print(A[cont], end=' ')
print(']')

print('B = [', end='')
for cont in range (0, len(B)):
    print(B[cont], end=' ')
print(']')

print('C = [', end='')
for cont in range (0, len(C)):
    print(C[cont], end=' ')
print(']')

14) Faça um programa que seja capaz de solicitar 6 nomes ao usuário, armazenando-os em um vetor chamado nomes. 
Após informar os nomes, o programa deve ser capaz de criar um segundo vetor chamado nomesInvertidos que contenha 
os mesmos valores de nomes, mas em ordem inversa. Por exemplo:
    nomes Maria José Carol Carlos Zenir Adão nomesInvertidos Adão Zenir Carlos Carol José Maria 
    Apresente ao usuário todos os valores de nomes e todos os valores de nomesInvertidos.
nomes = [''] * 6
nomesInvertidos = [''] * 6
contador = len(nomes) - 1

for cont in range (0, len(nomes)):
    nomes[cont] = input('Digite um nome: ')

cont = 0
while (contador >= 0):
    nomesInvertidos[cont] = nomes[contador]
    contador -= 1
    cont += 1

print('Nomes: ', nomes)
print('NomesInvertidos: ', nomesInvertidos)

15) Faça um programa que solicite ao usuário por 10 números inteiros. 
Após preencher os 10 números inteiros, o programa deve exibir uma mensagem informando quantos 
destes números são pares e quantos destes números são ímpares.
vetor = [0] * 10
numPares = 0
numImpares = 0

for cont in range (0, len(vetor)):
    vetor[cont] = int(input('Digite um número: '))

for cont in range (0, len(vetor)):
    if (vetor[cont] % 2 == 0):
        numPares += 1

    else:
        numImpares += 1

print('Vetor: ', vetor)
print('Esse vetor possui {} números pares e {} números ímpares.'.format(numPares, numImpares))

16) Uma empresa possui 8 funcionários. Um programa precisa ser desenvolvido para calcular o valor de 
aumento que será dado aos funcionários nos seus salários. Implemente um programa que solicite pelos nomes
dos funcionários e pelo salário de cada funcionário. Em seguida, atualize cada salário com um aumento de 15 % .
Por fim, exiba ao usuário a lista dos nomes, salários atuais e novos salários após o aumento.
funcionarios = [''] * 8
salarios = [0] * 8
novosSalarios = [0] * 8

for cont in range (0, len(funcionarios)):
    funcionarios[cont] = input('Funcionário: ')
    salarios[cont] = float(input('Salário: '))
    novosSalarios[cont] = salarios[cont] * 1.15

print('Nomes\t\tSalário atual\t\tNovo salário')

for cont in range (0, len(funcionarios)):
    print(funcionarios[cont], '\t\t', salarios[cont], '\t\t', novosSalarios[cont])

17) Faça um programa que solicite pelo nome completo de uma pessoa. Em seguida, apresente na tela:
nome = input('Digite seu nome completo: ')
nome = nome.lower()

    a) quantas vogais este nome possui
    Ex: “Dino da Silva Sauro” possui 8 vogais
vogais = 0

for cont in range (0, len(nome)):
    if (nome[cont] == 'a' or nome[cont] == 'e' or nome[cont] == 'i' or nome[cont] == 'o' or nome[cont] == 'u'):
        vogais += 1
print('Seu nome possui {} vogais.'.format(vogais))

    b) quantas letras n(ou N) ou a(ou A) este nome possui(contar os ‘n’ e os ‘a’)
    Ex: “Dino da Silva Sauro” possui 4 letras m ou a 
letras = 0

for cont in range (0, len(nome)):
    if (nome[cont] == 'n' or nome[cont] == 'a'):
        letras += 1

print(nome, 'possui {} letras n ou a'.format(letras))
    
    c) quantos espaços em branco este nome possui
    Ex: “Dino da Silva Sauro” possui 3 espaços em branco
branco = 0

for cont in range(0, len(nome)):
    if (nome[cont] == ' '):
        branco += 1

print(nome, 'possui {} espaços em branco'.format(branco))

18) Implemente um algoritmo que seja capaz de fazer a rotação para a esquerda de um vetor, como visto a seguir: 
vetor 4 2 8 48 -25 
[0] [1] [2] [3] [4] 
vetor2 2 8 48 -25 4 
[0] [1] [2] [3] [4] 
vetor = [4, 2, 8, 48, -25]
vetor2 = [0] * 5
cont = 0

while (cont < len(vetor)):
    if (cont == 0):
        vetor2[len(vetor2) - 1] = vetor[0]
    
    else:
        vetor2[cont - 1] = vetor[cont]
    cont += 1

print(vetor)
print(vetor2)

19) Um número é chamado de primo caso este número seja divisível apenas por 1 e por ele mesmo. Por
exemplo:
Número 2 é primo. Temos que 2 ÷ 1 = 1 e 2 ÷ 2 = 1.
Número 17 é primo. Temos que 17 ÷ 1 = 17 e 17 ÷ 17 = 1.
Número 6 não é primo. Temos que 6 ÷ 1 = 6, 6 ÷ 2 = 3, 6 ÷ 3 = 2 e 6 ÷ 6 = 1.
Para calcular se um número é primo ou não, portanto, podemos ter um algoritmo como segue:
num = 4
totalDivisao = 0
cont = 1
while (cont <= num):
if (num % cont == 0):
totalDivisao = totalDivisao + 1
cont = cont + 1
if (totalDivisao <= 2):
print("O numero", num, "é primo")
else:
print("O numero", num, "não é primo")
Um programa precisa ser desenvolvido de forma que diversos números inteiros possam ser fornecidos.
Desenvolva este programa, solicitando inicialmente ao usuário quantos números ele deseja fornecer. Em
seguida, o programa deve solicitar por estes números. Ao final, apresente ao usuário quantos destes números
são primos e quantos destes números não são primos
tamanho = int(input('Quantos números você deseja fornecer? '))
vetor = [0] * tamanho
numPrimos = 0
naoPrimos = 0

for i in range(0, tamanho):
    vetor[i] = int(input('Digite um número: '))
    totalDivisao = 0
    cont = 1
    while (cont <= vetor[i]):
        if (vetor[i] % cont == 0):
            totalDivisao = totalDivisao + 1
        cont = cont + 1
    if (totalDivisao <= 2):
        numPrimos += 1
    else:
        naoPrimos += 1

print('A quantidade de números primos é {}, e quantidade de não primos é {}'.format(numPrimos, naoPrimos))

20) Considere o seguinte conjunto de valores a serem armazenados em um vetor:
Vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Um programa precisa ser desenvolvido, de forma que o seguinte menu seja apresentado ao usuário:
MENU DE OPÇÕES:
a) Exibir números
b) Consultar número
c) Alterar número pelo índice
d) Alterar número pela ocorrência
e) Sair
Quando o usuário escolher a opção (a), os números do vetor devem ser apresentados.
Quando o usuário escolher a opção (b), o sistema deverá solicitar por um número ao usuário e, em seguida,
apresentar se este número está presente ou não no conjunto de valores, além de quantas ocorrências deste
número foram encontradas.
Quando o usuário escolher a opção (c), o sistema deverá solicitar qual o índice do vetor deverá ser modificado
e também qual será o novo valor, para então atualizar o vetor com o novo valor informado na posição desejada.
Quando o usuário escolher a opção (d), o sistema deverá solicitar por um número ao usuário e por um novo
número atualizado. Em seguida, todas as ocorrências do número no vetor devem ser substituídas pelo novo
número atualizado.
O sistema exibirá o menu e fará as suas respectivas ações até que o usuário informe a opção (e). Caso uma
opção diferente das exibidas no menu, o sistema deve exibir uma mensagem “Opção inválida, tente
novamente”
vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
opcao = 'f'

while (opcao != 'e'):
    '''
    print('''
    MENU DE OPÇÕES:
    a) Exibir números
    b) Consultar número
    c) Alterar número pelo índice
    d) Alterar número pela ocorrência
    e) Sair
    ''')
    '''
    opcao = input('Sua opcao: ')

    if (opcao == 'a'):
        for cont in range (0, len(vetor)):
            print(vetor[cont], end=' ')
        print('')

    elif (opcao == 'b'):
        ocorrencia = 0
        inicio = 0
        fim = len(vetor) - 1
        num = int(input('Digite o número a ser buscado: '))
        while(inicio <= fim):
            meio = int((inicio + fim)/2)
            
            if (vetor[meio] == num):
                posicao = meio
                ocorrencia += 1
                break

            elif (num < vetor[meio]):
                fim = meio -1
            
            else:
                inicio = meio + 1
            
        if (ocorrencia >= 1):
            print('O número procurado apareceu {} vezes'.format(ocorrencia))

        else:
            print('Número não encontrado')

    elif (opcao == 'c'):
        indice = int(input('Digite o índice a ser mudado: '))
        valor = int(input('Digite o valor a ser alterado: '))
        vetor[indice] = valor
        print('O novo vetor agora é ', vetor)

    elif (opcao == 'd'):
        num = int(input('Digite o número a ser substituído: '))
        valor = int(input('Digite o valor atualizado: '))
        posicao = -1
        inicio = 0
        fim = len(vetor) - 1

        while (inicio <= fim):
            meio = int((inicio + fim) / 2)

            if (num == vetor[meio]):
                vetor[meio] = valor
            
            elif(num < vetor[meio]):
                fim = meio - 1

            else:
                inicio = meio + 1
        
        print('O novo vetor é ', vetor)

    else:
        print('Opção inválida! Tente novamente!')


'''