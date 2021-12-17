"""
Faça um algoritmo que pergunte ao usuário quantos números ele quer somar e que peça pra ele inserir os N números. 
O programa deve informar a soma total dos números informados.
"""
n = int(input("Quantos numero para somar"))

cont = 1
soma = 0
while cont < n+1:
   soma += int(input("Digite um numero:" ))
   cont += 1

print(soma)