# coding: utf-8

'''
Created on 10/12/2012

@author: ikarus
'''
import multiprocessing
import sys
import math
from sesion import *
from generador import * 

'''
Opciones:
-fichero <nombre_fichero> (obligatorio)
-min <longitud_minima_palabra> (obligatorio)
-max <longitud_maxima_palabra> (obligatorio)
-desde <palabra_de_inicio> (opcional)
'''

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
tareas = []
sesion = Sesion(alfabeto)

if (sesion.comprobacionArgumentos(sys.argv)):
    generador = Generador(sesion.fichero, sesion.alfabeto, sesion.min, sesion.max, sesion.desde)
    proceso = multiprocessing.Process(target=generador.getCombinaciones)
    tareas.append(proceso)
    proceso.start()
else:
    print "-- No se puede crear el diccionario --"
    

    
