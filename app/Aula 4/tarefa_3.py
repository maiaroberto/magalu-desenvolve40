"""
Faça uma função que recebe um dia da semana identificado como 0=Dom, 1=Seg, 2=Ter, ... 6=Sáb, 
e um booleano indicando se estamos ou não em férias. 
Retorne uma string na forma "HH:MM" indicando a hora em que o alarme deve tocar. 
Em dias de semana, o alarme deve tocar às "07:00" e nos fins de semana, o alarme deve tocar às "10:00".
A menos que estejamos de férias. Neste caso, em dias de semana, o alarme deve tocar às "10:00" 
e em fins de semana a resposta do alarme deve ser "off".
"""
def alarme(dia, ferias):
    hora = ""
    if dia in [1,2,3,4,5]:
        hora = "10:00" if ferias else "07:00"
    else:
        hora = "off" if ferias else "10:00"
    return hora

print(alarme(6, False))