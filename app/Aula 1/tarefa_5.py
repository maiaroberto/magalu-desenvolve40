# Faça um programa que leia o salário mensal atual de um funcionário e o percentual de reajuste. 
# Calcule e escreva o valor do novo salário.

salario = float(input("Digite o salario mensal: ")) 
reajuste = float(input("Digite o percentual de reajuste: ")) 
novoSalario = float(salario * (reajuste / 100 + 1)) 
print(f"Novo Salario = R$ {novoSalario:.2f}")
