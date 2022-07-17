"""
Tipo Booleano

Algebra Booleana, criada por George Boole
2 constantes, Verdadeiro ou Falso

True => Verdadeiro
False => Falso

OBS: Sempre com a inicial maiúscula

Errado:

true, false

Certo:

True, False
"""

# Usuário esta ativo ou não no sistema

ativo = False
print(ativo)

"""
Operações Básicas:

"""
"""
Negação (not)

Fasendo a negação:

 Se o valor booleano for verdadeiro o resultado sera falso
 Se o valor booleano for falso o resultado sera verdadeiro. 
Ou seja sempre o contrário.
  
"""
# A variavel (ativo) esta False colocando not sera True

print(not ativo)
logado = False

"""
Ou (or)

Uma operação binária, ou seja, depende de dois valores:

ou um ou o outro devem ser verdadeiro.

True or True  =>  True  
True or False =>  True 
False or True =>  True   
False or False =>  False 
"""
# Usuário esta logado no sistema?

# ativo esta False logado False => RESULTADO  FALSE
# ativo estivesse true logado Fale => RESELTADO SERIA TRUE
# ativo estivesse False logado True => RESELTADO SERIA TRUE
# ativo estivesse true logado True => RESELTADO SERIA TRUE

print(ativo or logado)

"""
E (and):

Também é uma operação binária, ou seja, depende de dois valores. 
Ambos os valores devem ser verdadeiro.

True or True  =>  True
True or False =>  False
False or True =>  False
False or Fale =>  False

"""
'''
5 > 6  False
5 < 6  True
6 == 6 True
4 <= 5 True
'''
num1 = 7 
num2 = 8 
num1 >= num2
num1 == num2
print(num1 <= num2 or num1 > 3)
print(num1 < num2 and num1 > 3)

"""
type(True)
(bool)

type(False)
(bool)

type(Ativo)
(bool)

dir(Ativo)
Mostraeá todas as opções disponíveis 
"""
