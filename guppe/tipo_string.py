"""
Tipo String
Em Python, um dado tipo STRING fica entre aspas simples:
'uma string', '24', 'a', 'True', '4.3'

Em Python, um dado tipo STRING fica entre aspas duplas:
"uma string", "24", "a", "True", "4.3"

Em Python, um dado tipo STRING fica entre aspas simples triplas:
'''uma string''', '''24''', '''a''', '''True''', '''4.3'''

Em Python, um dado tipo STRING fica entre aspas duplas triplas:
# """""", """""", """""", """""", """"""

"""
nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

# Quebra a linha

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

# Quebra a linha

nome = """Angelina 
Jolie"""
print(nome)
print(type(nome))


nome = "Angelina \"Jolie"
print(nome)
print(type(nome))

# TUDO MAIÚSCULO
nome = 'Geek University'
print(nome.upper())

# tudo minúsculo
nome = 'Geek University'
print(nome.lower())

# Criar lista de strings
nome = 'Geek University'
print(nome.split())


# Como Python divide as palavras
#[ 0,   1,   2.   3,  4.  5,   6,   7,   8,   9,  10,  11,  12,   13,  14]
#['G', 'e', 'e', 'k, ' ' ,U' ,'n', 'i'. 'v', 'e', 'r', 's', 'i', 't', 'y']
# Achando as posições na lista letra por letra
print(nome[0:4]) # Slice de tring
print(nome[5:15]) # Slice de tring


# Como Python divide as Frases
# [  0,        1]
# ['Geek','University']
print(nome.split()[0])
print(nome.split()[1])
# Achando as posições na lista dividindo as frases


# [::-1] => Comece do primeiro elemento, vá até o último e inverta
print(nome[::-1])

# Trocar as letras de uma lista
print(nome.replace('G', 'P'))
print(nome.replace('E', 'I')) # Troca todos os 'e' repetiodos por 'i'

texto = 'socorram me subino em marrocos' # Palindromo
print(texto[::-1])
