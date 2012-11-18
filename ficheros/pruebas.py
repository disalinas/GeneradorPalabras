'''
Created on 18/11/2012

@author: ikarus
'''
from funciones import *

alfabeto = ['a','b','c']
print "Alfabeto:"
print alfabeto
print "Obteniendo permutaciones..."
permTotales = math.factorial(len(alfabeto))
permutaciones = getPermutaciones(alfabeto)
print "--- PERMUTACIONES OBTENIDAS PARA [a,b,c] ---"
print "Permutaciones totales obtenidas " + str(len(permutaciones)) + " de " + str(permTotales)
print permutaciones

alfabeto = ['a','b','c','d']
print "Alfabeto:"
print alfabeto
print "Obteniendo permutaciones..."
permTotales = math.factorial(len(alfabeto))
permutaciones = getPermutaciones(alfabeto)
print "--- PERMUTACIONES OBTENIDAS PARA [a,b,c,d] ---"
print "Permutaciones totales obtenidas " + str(len(permutaciones)) + " de " + str(permTotales)
print permutaciones

alfabeto = ['a','b','c','d','e']
print "Alfabeto:"
print alfabeto
print "Obteniendo permutaciones..."
permTotales = math.factorial(len(alfabeto))
permutaciones = getPermutaciones(alfabeto)
print "--- PERMUTACIONES OBTENIDAS PARA [a,b,c,d,e] ---"
print "Permutaciones totales obtenidas " + str(len(permutaciones)) + " de " + str(permTotales)
print permutaciones

alfabeto = ['a','b','c','d','e','f']
print "Alfabeto:"
print alfabeto
print "Obteniendo permutaciones..."
permTotales = math.factorial(len(alfabeto))
permutaciones = getPermutaciones(alfabeto)
print "--- PERMUTACIONES OBTENIDAS PARA [a,b,c,d,e,f] ---"
print "Permutaciones totales obtenidas " + str(len(permutaciones)) + " de " + str(permTotales)
print permutaciones

alfabeto = ['b','e','d','i','x','o','c']
print "Alfabeto:"
print alfabeto
print "Obteniendo permutaciones..."
permTotales = math.factorial(len(alfabeto))
permutaciones = getPermutaciones(alfabeto)
print "--- PERMUTACIONES OBTENIDAS PARA [a,b,c,d,e,f] ---"
print "Permutaciones totales obtenidas " + str(len(permutaciones)) + " de " + str(permTotales)
print permutaciones