"""
4) Faça a somatória de todos os numeros seguindo a sequência:

11+12+13+14+15+16+...+11000
"""

soma = 0.0
cont = 1
while cont < 1001:
   soma += 1/cont
   cont += 1

print(soma)
