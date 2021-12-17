"""
Faça um programa que pede para o usuário digitar 5 números e, ao final,
 imprime uma lista com os 5 números digitados pelo usuário
"""

n = 5 
cont = 1
texto = []
while cont < n+1:
   texto.append(int(input("Digite um numero:" )))
   cont += 1

print(texto)    