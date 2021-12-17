# 1) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#
#Álcool:
#
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro.
#
#Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é 2,50 reais 
# o preço do litro do álcool é 1,90 reais.

alcool20 = .03
alcoolMais = .05

gas20 = .04
gasMais = .06

alcool = 1.90
gas = 2.50

litros = float(input("número de litros vendidos: "))
tipoCombustivel = input("Tipo de Combustivel A-álcool, G-gasolina):")

valorPago = 0.0

if tipoCombustivel == "A" or tipoCombustivel == "a":
    valorPago = litros * alcool
    if litros > 20:
        valorPago -= valorPago * alcoolMais
    else:
        valorPago -= valorPago * alcool20
elif tipoCombustivel == "G" or tipoCombustivel == "g":
    valorPago = litros * gas
    if litros > 20:
        valorPago -= valorPago * gasMais
    else:
        valorPago -= valorPago * gas20
else: 
    print("Tipo de Combustivel invalido")
    
print(f"valor a ser pago R$ {valorPago:.2f}")    