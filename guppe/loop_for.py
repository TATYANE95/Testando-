"""
Loop for
Loop -> Estrutura de repetição.
For -> Uma dessas estruturas.

C ou JAVA

for(int i = 0; i < 10; i++){
   // execução do loop
}
Python

for item in interavel:
    //execução do loop

Utilizmos loops para iterar sobre sequênsias ou sobre valores iteraveis

Exemplos de iteraveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
     numeros = range(1, 10)
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando em uma lista)
for numeros in lista:
    print(numeros)

# Exemplo de for 3 (Iterando em uma range)
for numeros in range(1, 10):
    print(numeros)
"""
range(valor_inicial, valor_final)
OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não
"""

"""
Enumerate:

((0, 'G'), (1, 'e'), (3, 'e'), (4, 'k'), (4 ''), ...)

"""

# 1
for indice, letra in enumerate(nome):
    print(nome[indice])
# 2
for indice, letra in enumerate(nome):
    print(letra)
# 3
for _, letra in enumerate(nome):
    print(letra)
# 4
for valor in enumerate(nome):
    print(valor)
# 5
for valor in enumerate(nome):
    print(valor[1])
    print(valor[0])

qtd = int(input('Quantas vezes esse loop deve rodar? '))
# 6
for n in range(1, qtd + 1):  # Se tirar o +1 o loop vai de (1 até 4) com o +1 ele vai de (1 até 5)
    print(f' Imprimindo {n}')

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
# 7
for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n} / {qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')
"""
Outro exemplos no console:

nome = 'Geek'
nome + ' University'
('Geek University')

nome * 3
('GeekGeekGeek')
nome * 13
('GeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeek')
nome * 330
('GeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeekGeek...')

"""
# Original: U+1F605
# Modificado: U0001F605

for _ in range(3): # faz o loop 3 vezes
    for num in range(1, 11):
        print('\U0001F605' * num)
# Clicar no print + CTRL mostra as opções como no Help
