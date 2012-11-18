import math

def getPermutaciones(alfabeto):
    permutaciones = []
    for letra in alfabeto:
        lista = list(alfabeto)        
        lista.remove(letra)        
        devolucion = getPermutaciones(lista)
        
        if len(devolucion) > 0:
            for permutacion in devolucion:
                permutaciones.append(letra + permutacion)
        else:
            permutaciones.append(letra)
    return permutaciones

