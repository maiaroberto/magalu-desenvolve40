# 2) Faça um Programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4

print(f"Media das notas {n1}, {n2}, {n3} e {n4} é igual a {media}")