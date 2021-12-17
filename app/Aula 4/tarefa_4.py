"""
Faça uma função que recebe dois inteiros a e b e retorna a potência a^b sem utilizar o operador **.
"""
def potencia(base,expoente):
    contador = 1
    valor = 1
    while contador <= expoente:
        valor *= base
        contador+=1
        
    return valor

print(potencia(3,3))