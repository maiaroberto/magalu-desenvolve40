"""
Faça uma função que recebe um texto e um letra e retorne a quantidade daquela letra naquele texto
 (ignore diferenças de capitalização, 'A' e 'a' são a mesma letra)
"""
def contaLetras(texto, letra):
    conta = 0
    cont = 0
    while cont < len(texto):
        if texto[cont] == letra: conta +=1 
        cont += 1    
    return conta

texto = "asdf asdf asdf asdaaa"
letra = "a"

print(contaLetras(texto, letra))
