"""
Faça uma função que recebe um inteiro n e retorna uma lista com os n primeiros elementros da sequência de fibonacci

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
"""
def fibo(n):
    u_1 = 1
    u_2 = 1
    count = 0

    lista = [1,1]

    for vic in range(0, n-2):
        count = u_1 + u_2
        u_1 = count
        u_2 = (count - u_2)
        lista.append(count)

    return(lista)

n = int(input('Inserir numero para gerar a sequência de Fibonnaci :'))

print(fibo(n))
