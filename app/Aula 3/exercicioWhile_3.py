"""
3) Escreva um programa que encontra o maximo divisor comum entre dois números
"""

print("calcular o MDC entre dois números")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

a = n1
b = n2
while b != 0:
    resto = a % b
    a = b
    b = resto

print(f"O o maximo divisor comum entre {n1} e {n2} é {a}")