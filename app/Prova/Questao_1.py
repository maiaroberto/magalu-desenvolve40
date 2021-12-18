"""
Questão #1
Vale
20
Enunciado
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Fruta	Até 5kg	    Acima de 5kg
Morango	R$2,50/kg	R$2,20/kg
Maçã	R$1,80/kg	R$1,50/kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.

Escreva uma função que receba a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas e retorne o valor a ser pago pelo cliente.

Não é necessário validar os dados de entrada. Assuma o enunciado.
"""
def valorPago(morango, maca):
    
    pago  = 2.50 * morango if morango < 5 else 2.20 * morango
    pago += 1.50 * maca    if maca    < 5 else 1.50 * maca
    peso = morango + maca
    desconto = .90 if peso > 8 or pago > 25 else 1
    valor = pago * desconto
    return valor
    
print(f"valor a ser pago pelo cliente R$ {valorPago(8, 0):.2f}")
