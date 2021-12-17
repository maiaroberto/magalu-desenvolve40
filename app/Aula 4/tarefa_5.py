"""
Faça uma função que receba as coordenadas de dois pontos cartesianos no formato de duas listas [x1, y1] e [x2, y2] 
e retorne a distância euclidiana entre os pontos com 2 casas decimais.
"""

def distancia(ponto1,ponto2):
    dif_x = (ponto1[0]-ponto2[0])**2
    dif_y = (ponto1[1]-ponto2[1])**2
    return (dif_x + dif_y)**0.5
    
print(distancia([-2,5],[4,-3]))
