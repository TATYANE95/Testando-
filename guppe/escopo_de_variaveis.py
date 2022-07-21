"""
Escopo de variáveis

Dois casos de escopo:

1- Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreendido, todo o programa.

2- Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está
    limitado apenas ao bloco onde foi declarada.


Python é uma linguagem se tipagem dinâmica.
Isso que ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""
"""
ESSE É UM EXEMPLO DE VARIÁVEL GLOBAL
"""
# Resultado sera tipo 'int'/inteiro
numero = 42
print(numero)
print(type(numero))

# Resultado sera tipo 'str'/string
numero = 'Geek'
print(numero)
print(type(numero))


# Ex: print(não_existo)
# tem que atribuir sempre um valor como:
não_existo = 'oi'
print(não_existo)

"""
ESSE É UM EXEMPLO DE VARIÁVEL LOCAL
"""
# Nesse exemplo (novo) entrará no sistema pois valor de (numero) corresponde aos requisitos do sistema porem mesmo assim ele é local
numero = 42

if numero > 10:
    novo = numero + 10 # Vareável (novo) declarada localmente dentro do bloco if
    print(novo)
# Agora como o valor de (numero) é menor do que a condição o sistema encerra e (novo) nunca entrara globalmente para que seu valor seja usado novamente
numero = 2

if numero > 10:
    novo = numero + 10
    print(novo)

# Para entrar globamente novo precisa ser declarado mesmo assim se a condição for menor o valor não estará correto
# Forma errada
numero = 2
novo = 0
if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)
# Forma correta
numero = 42
novo = 0 # Vareável (novo) declarada globalmente fora do bloco if
if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)