print('''
*-*-* CADASTRO DE ALUNOS *-*-*
1. Cadastrar
2. Alterar
3. Excluir
4. Consultar
5. Imprimir Relatório
''')
escolha = input('Digite sua escolha: ')

if (escolha == '1'):
    print('Você escolheu a opção 1 - Cadastrar')
elif (escolha == '2'):
    print('Você escolheu a opção 2 - Alterar')
elif (escolha == '3'):
    print('Você escolheu a opção 3 - Excluir')
elif (escolha == '4'):
    print('Você escolheu a opção 4 - Consultar')
elif (escolha == '5'):
    print('Você escolheu a opção 5 - Imprimir Relatório')
else:
    print('Opção inválida!')
