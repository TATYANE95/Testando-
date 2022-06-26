"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para a lingusgem Python
The Zen of Python
import this
A ideia da PEP8 é que possamos escrever codigos Python de forma Pythonica.
[1] - Utilize Camel Case para nomes de classes;

ou variaveis;



class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize nomes em minùsculo, seprandos por underline paou variaveis;

def soma():
    pass

def sama_dois():
    pass

numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identaçâo!

if 'a' in 'banana' :
    print('tem')
[4] - Linhas em branco]
-Separar funçôes e definições de classe com duas linhas em branco;
-Metodos dentro de uma classe devem ser separados com uma unica linha em branco;


class Classe:
    pass


class Outra:
    pass

[5] -Imports
-imports devem ser sempre feitos em linhas separados;

# Import Errado

import sys. os

# Import Correto

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrings e antes de constantes ou variáveis globais.

[6] - Espaços em expressões e instruções


# Nâo faça:

funcao( algo[ 1 ]. { outro: 2 } )

# Faça:

funcao(algo[1], {outro: 2})

# Nâo faça:

algo (1)

# Faça:

algo(2)

# Nâo faça:

dict ['chave'] = list [indice]

# Faça:

dict['chave'] = list[indice]

# Nâo faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
y = 3
variavel_longa = 5
[7] - Termine sempre uma instrução com uma nova linha
"""
import this
