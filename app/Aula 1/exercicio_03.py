# 3) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

valorHora = float(input("Valor da Hora trabalhada: "))
numeroHoras = float(input("Número de Horas no mês: "))
salario = valorHora * numeroHoras
print(f"Salario no mês = {salario:.2f}")