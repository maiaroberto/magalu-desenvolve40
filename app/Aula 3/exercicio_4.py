"""
Faça um programa que escreva todos os números múltiplos de 7 entre 1 e N,
sendo N um valor positivo e inteiro introduzido pelo utilizador. 
Por exemplo: se N = 40, o programa deve imprimir: 7 14 21 28 35
"""
n = int(input("Digite um numero:" ))
cont = 1
while cont < n:
   if cont % 7 == 0:   
      print(cont)
   cont += 1