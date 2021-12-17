"""
Dada uma lista encadeada de caracteres formada por uma seqüência alternada de letras e dígitos, construa um método que retorne uma lista na qual as letras são mantidas na seqüência original e os dígitos são colocados na ordem inversa. Exemplos:

A 1 E 5 T 7 W 8 G
®: A E T W G 8 7 5 1

3 C 9 H 4 Q 6
®: C H Q 6 4 9 3

Como mostram os exemplos, as letras devem ser mostradas primeiro, seguidas dos dígitos. Sugestão:
usar método isdigit() que retorna booleano que retorna verdadeiro caso um caractere seja um dígito.
"""
lista = "A1E5T7W8G"
cont = 0
letras = []
numeros = []
while cont < len(lista):
   
   if lista[cont].isdigit():
      numeros.insert(0, lista[cont])
   else:
      letras.append(lista[cont]) 
   cont += 1

print(letras + numeros)
