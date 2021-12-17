#4) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# 𝐶=5∗(𝐹−32)9

fahrenheit = float(input("Temperatura em graus Fahrenheit: "))
celsius = (5 * (fahrenheit -32)) / 9
print(f"{fahrenheit:.1f}° fahrenheit é igual a {celsius:.1f}° Celsius")