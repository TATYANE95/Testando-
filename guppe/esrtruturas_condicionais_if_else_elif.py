"""
Estruturas condicionais
if (Se), else (se não), elif(se não se)
# não precisa de parênteses após if, else e elif


# Estrutura condicional if em C

if(idade < 18){
    printf("menor de idade");


# Estrutura condicional if, else em Java

if(idade <18){
    System.out.printIn("Menor de idade");
}else{
   System.out.print("Maior de idade");
}

"""

# Caso colocar idade = 26 não vai validar, para isso temos que colocar o ()

idade = 18

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('tem 18 anos')
else:
    print('maior de idade')
