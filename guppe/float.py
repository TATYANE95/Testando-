"""
Tipo Float ou tipo real.decimal
Casas decimais

OBS: SEPARADOR É COM PONTO E NÃO VÍRGULA.
"""

# Errado do ponto de vista do float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))
# Certo do ponto de vista do FLoat
valor = 1.44
print(valor)
print(type(valor))

#É possível fazer dupla atribuição
valor1, valor2 = 1,44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

#Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiro perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))


salario1 = 2.56
salario2 = 3.67
total = salario1 + salario2
print(total)
# Total Float 6.23
total = int(salario1) + int(salario2)
print(total)
# Total int 5
print(dir(total))

# Podemos trabalhar com números complexos

variavel = 5j
print(type(variavel))
print(variavel)