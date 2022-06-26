"""
Recebendo dados do usuário
"""
# Entrada de dados
#print("Qual é o seu nome? ")
#nome = input() # input ->entrada de dados do usuario
nome = input("Qual é o seu nome? ")
# Processamento

#Saída de dados
#ex antigo
#print('Seja bem-vindo(a) %s' % nome)
print (f'Seja bem-vindo(a) {nome}')
#1 Entrada de dados
#print("Qual é a sua idade? ")
#idade = input() # input ->entrada de dados do usuario
#2 Entrada de dados
idade = int(input("Qual é a sua idade? "))# FORMA 2 idade = input("Qual é a sua idade? "))
#Exemplo print 'antigo' versão 2....
#print ('A %s tem %s anos' % (nome, idade))
#Exemplo print 'moderno' versão 3....
#print('A {0} tem {1} anos' .format(nome, idade))
#Exemplo print 'atual' versão 3.7
print(f'A{nome} tem {idade} anos')

#int(idade) => cast
#Cast é a 'conversão' de um tipo de dado para outro.
#Forma 1
#print(f'A {nome} nasceu em {2022 - int(idade)}')
#Forma 2 Transformar a idade string em inteiro para dvolver o valor da subtrção em numero inteiro levando o Int para idade
print(f'A {nome} nasceu em {2022 - (idade)}')

#Ex string
#Aspas simples ->'Tatiane'
#Aspas duplas ->"Tatiane"
#Aspas simples triplas ->'''Tatiane'''
#Aspas duplas triplas ->"""Tatiane"""