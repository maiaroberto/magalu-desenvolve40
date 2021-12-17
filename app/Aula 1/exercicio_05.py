# 5) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# 
# Salário bruto.
# Quanto pagou de IR
# Quanto pagou ao INSS.
# Quanto pagou ao sindicato.
# O salário líquido.

valorHora = float(input("Valor da Hora trabalhada: "))
numeroHoras = float(input("Número de Horas no mês  : "))

salario = valorHora * numeroHoras
ir = salario * 0.11
inss = salario * 0.085
sindicato = salario * 0.05
liquido = salario - (ir + inss + sindicato)

print("TOTAIS:")
print(f"Salario Bruto = {salario:8.2f}")
print(f"IR           -= {ir:8.2f}")
print(f"INSS         -= {inss:8.2f}")
print(f"Sindicato    -= {sindicato:8.2f}")
print(f"Liquido       = {liquido:8.2f}")