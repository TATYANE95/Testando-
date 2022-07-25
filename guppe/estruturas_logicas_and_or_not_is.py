"""
Estruturas Lógicas: and (e), or(ou), not(não), is(é)

Operadores unários:
 - not
Operadores binários:
 - and, or, IS
"""


# AND ambos os valores tem que ser verdadeiro para emprimir na primeira linha do bloco
# caso um dos dois valores seja FALSE independente se o outro valor é TRUE sera emprimido a
ativo = True
logado = True

if ativo and logado:
    print('Bem vindo usuário!')
else:
    print('Voce precisa ativar sua conta. Por favor, cheque seu e´mail')


# OR um ou outro valor tem que ser verdadeiro
# mas tem problema ambos forem verdadeiros
# caso os dois valores sejam falsos não ira funcionar
if ativo and logado:
    print('Bem vindo usuário!')
else:
    print('Voce precisa ativar sua conta. Por favor, cheque seu e´mail')


# NOT inverte o valor ou seja:
if not ativo:
    # Se não estiver ativo (False) escreva isso
    print('Voce precisa ativar sua conta. Por favor, cheque seu e-mail')
else:
    # Se estiver ativo (true) escreva isso
    print('Bem vindo usuário!')


# IS é para comparar um valor com o outro mesma coisa que (1 == 1)
if ativo:
    print('Bem vindo usuário!')
else:
    print('Voce precisa ativar sua conta. Por favor, cheque seu e-mail')

# ativo è true?
print(ativo is True)


# nome = 'Geek' / dir nome
# nome.istitle() False
# nome.isupper() True
# nome =  geek / nome.istitle() FALSE
