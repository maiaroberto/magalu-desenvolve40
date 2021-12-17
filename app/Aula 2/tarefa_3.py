# Faça um programa que leia 3 números e informe o maior deles

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior = numero1
if numero2 >= maior: maior = numero2
if numero3 >= maior: maior = numero3

print("A maior numero é", maior) 