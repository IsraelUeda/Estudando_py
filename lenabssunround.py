"""
Len, abs, Sum e Round

len() retorna o tamanho, ou seja, o numero de itens de um iteravel
#por deibaixo dos panos o python faz o squint __len__()

#quando tem dois __ se chama dunder
abs() retorna o valor absoluto de um numero inteiro ou real, de forma básica se´ria seu valor sem o sinal


print(abs(4))
print(abs(-4))
print(abs(10))
print(abs(9.32))

#sum() recebe como parametro um iteravel podendo conter um valor inicial, e retorna a soma total
dos elementos incluindo o valor iniciar

obs: o valor inicial default é 0



print(sum(range(1,90),10))
print(sum(range(1,90))) 

#round retonra um numero arredondado para n digito de precisão apos a casa decimal, se aprecisão não for infiormada
retorna o inteiro + proximo da entrada


"""
print(round(9.65))
print(round(9.35))
print(round(9.51))
print(round(9.49))
print(round(9.50, 2))  