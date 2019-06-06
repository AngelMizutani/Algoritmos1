'''
1.Crie um vetor e armazene os números de 1 a 100.
Cada número deve ocupar uma posição do vetor (lista).
Obs. O vetor criado aqui será utilizado do “a” ao “f”. Não precisa ficar criando ele novamente toda hora.
vetor = [0] * 100
cont = 0

# while (cont < len(vetor)):
#     vetor[cont] = cont + 1
#     cont += 1

for cont in range(0, len(vetor)):
    vetor[cont] = cont + 1
    cont += 1

a) Mostre na tela todos os números do vetor em ordem crescente (1 a 100).
print(vetor)

b) Mostre na tela todos os números do vetor em ordem decrescente (100 a 1).
contador = 99
while (contador >= 0):
    print(vetor[contador], end=', ')
    contador -= 1

c) Mostre na tela o dobro de todos os números.
vetorDobro = [0] * 100
for cont in range (0, len(vetor)):
    vetorDobro[cont] = vetor[cont] * 2
    cont += 1
print(vetorDobro)

d) Apresente na tela a soma de todos os números.
soma = 0
for cont in range (0, len(vetor)):
    soma += vetor[cont]
    cont += 1
print(soma)

e) Apresente na tela a média geral dos valores contidos na lista.
soma = 0
for cont in range (0, len(vetor)):
    soma += vetor[cont]
    cont += 1
print('Média: ', soma / 100)

f) Mostre na tela a quantidade de números pares.
qtdePares = 0
for cont in range(0, len(vetor))):
    if (vetor[cont] % 2 == 0):
        qtdePares += 1
    cont += 1
print('O número de pares é ', qtdePares)

2. Faça um programa para armazenar 6 números inteiros para uma loteria,
permitindo que o usuário informe os números sorteados.
Depois de preencher, informe uma mensagem e os números sorteados.
loteria = [0] * 6
for cont in range (0, 6):
    loteria[cont] = int(input('Informe o número sorteado: '))
    cont += 1
print('Os números sorteados foram: ', loteria)

3. Um professor precisa armazenar em uma lista os nomes dos alunos presentes em
um minicurso. Faça um programa para armazenar 5 nomes e permitir que o professor
digite o nome da cada um. Em seguida, apresente na tela todos os nomes informados.
nome = [0] * 5
cont = 0
while (cont < 5):
    nome[cont] = input('Digite o nome do aluno: ')
    cont += 1
print('Alunos: ', nome)

4. Faça um programa que peça para o usuário informar o tamanho de um vetor.
Em seguida, crie este vetor e preencha ele com números digitados pelo usuário.
Por fim, apresente na tela os números digitados.
tamanho = int(input('Informe o tamanho do vetor: '))
vetor = [0] * tamanho
cont = 0
for cont in range(0, len(vetor)):
    vetor[cont] = int(input('Digite um número: '))
    cont += 1
print('Os números digitados foram: ', vetor)

5. Para os exercícios abaixo, utilize o vetor criado no exercício anterior.
a) Apresente os números do vetor em ordem inversa.
contador = len(vetor) - 1
while (contador >= 0):
    print(vetor[contador], end=' ')
    contador -= 1

b) Apresente a soma de todos os elementos.
soma = 0
contador = 0
while (contador < len(vetor)):
    soma += vetor[contador]
    contador += 1
# print('A soma dos elementos é ', soma)

c) Calcule a média aritmética dos valores.
media = soma / len(vetor)
print('A média aritmética dos valores é ', media)

d) Liste na tela somente os números do vetor que estão em posições (índices) pares.
for cont in range (0, len(vetor)):
    if (cont % 2 == 0):
        print(vetor[cont])
    cont += 1

e) Determinar um segmento informado pelo usuário (posição inicial e final)
para apresentar os números na tela. Por exemplo:
na sequência 5, 2, -2, -7, 3, 14, 10, -3, 9, -6, 4, 1 o usuário teria que
informar 4 e 8 (posição inicial e final, respectivamente) para mostrar na tela
somente os valores destacados.
inicial = int(input('Informe a posição inicial: '))
final = int(input('Informe a posição final: '))

posicao = inicial

while (posicao <= final):
    print(vetor[posicao])
    posicao += 1

f) Determinar um segmento informado pelo usuário (posição inicial e final)
para apresentar a soma daquele intervalo. Exemplo: Na sequência 5, 2, -2, -7, 3,
14, 10, -3, 9, -6, 4, 1 , a soma do segmento destacado é 33.
inicial = int(input('Informe a posição inicial: '))
final = int(input('Informe a posição final: '))

posicao = inicial
soma = 0

while (posicao <= final):
    soma += vetor[posicao]
    posicao += 1
print('A soma do segmento destacado é ', soma)

g) Encontre qual é o maior e o menor número desta lista.
maior = vetor[0]
menor = vetor[0]
cont = 0
while (cont < len(vetor)):
    if (vetor[cont] > maior):
        maior = vetor[cont]
    if (vetor[cont] < menor):
        menor = vetor[cont]
    cont += 1
print('O maior valor da lista é {}, e o menor valor é {}'.format(maior, menor))

h) Encontre qual é o maior e o menor número desta lista.
Além disso, informe quais são os índices (posições) deles.
posicaoMenor = 0
posicaoMaior = 0
maior = vetor[0]
menor = vetor[0]
cont = 0
while (cont < len(vetor)):
    if (vetor[cont] > maior):
        maior = vetor[cont]
        posicaoMaior = cont
    if (vetor[cont] < menor):
        menor = vetor[cont]
        posicaoMenor = cont
    cont += 1
print('O maior valor da lista é {}, na posição {}'.format(maior, posicaoMaior))
print('O menor valor é {}, na posição {}'.format(menor, posicaoMenor))

i) Informe quantos números pares e ímpares foram digitados
(apenas a quantidade de cada).
numPares = 0
numImpares = 0

for cont in range (0, len(vetor)):
    if (vetor[cont] % 2 == 0):
        numPares += 1
    else:
        numImpares += 1
    cont += 1

print('Foram digitados {} números pares e {} números ímpares.'.format(numPares, numImpares))

6. Crie um vetor para armazenar alguns números que serão utilizados
no cálculo da tabuada.
tamanho = int(input('Digite o tamanho do vetor: '))
vetor = [0] * tamanho

for cont in range (0, len(vetor)):
    vetor[cont] = int(input('Digite um número: '))
    cont += 1
print('Vetor:', vetor)

a) Apresente todos os números informados e seu respectivo dobro.
dobroVetor = [0] * tamanho
for cont in range (0, len(dobroVetor)):
    dobroVetor[cont] = vetor[cont] * 2
    cont += 1
print('Dobro dos valores: ', dobroVetor)

b) Para cada número presente no vetor, faça a tabuada do 1 ao 10
(utilizando laço de repetição).
for cont in range (0, len(vetor)):
    for contador in range (1, 11):
        print(vetor[cont], '*', contador, '=', vetor[cont] * contador)
        contador += 1
    print('')
    cont += 1
'''
'''
Um professor precisa armazenar uma lista de n alunos e seus respectivos conceitos. Crie um programa para auxiliar este professor.

Faça um programa para armazenar seis números inteiros para uma loteria, permitindo que o usuário informe os números sorteados. Em seguida, peça para o usuário informar os seis números que ele apostou. Por fim, apresente na tela quantos números ele acertou, informando se ele não ganhou nada (0 a 3 acertos), se acertou a quadra (4 acertos), a quina (5 acertos) ou se ele nunca mais vai precisar trabalhar (6 acertos).

Faça um programa para armazenar seis números inteiros para uma loteria, de modo que os seis números sejam criados aleatoriamente pelo Python e que não sejam repetidos. Em seguida, peça para o usuário informar os seis números que ele apostou. Por fim, apresente na tela quantos números ele acertou, informando se ele não ganhou nada (0 a 3 acertos), se acertou a quadra (4 acertos), a quina (5 acertos) ou se ele nunca mais vai precisar trabalhar (6 acertos).

Considerando que uma palavra (string) pode ser percorrida como um vetor, faça um programa que peça o nome de uma pessoa e o apresente de trás para frente.

Um esquema de sorteio precisar armazenar uma lista de 10 pessoas e ao final sortear uma delas aleatoriamente. Faça um programa para este esquema. (Dica: procure no Google como faz para gerar um número inteiro aleatoriamente no Python)

Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

	"Qual o melhor Sistema Operacional para uso em servidores?"
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

	Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     	-----   	---
Windows Server           1500   	17%
Unix                     	3500   	40%
Linux                    	3000   	34%
Netware                   	500    	5%
Mac OS                    	150    	2%
Outro                    	150    	2%
-------------------     	-----
Total                    	8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''
