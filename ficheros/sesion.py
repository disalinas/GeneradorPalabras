# coding: utf-8
'''
Created on 10/12/2012

@author: ikarus
'''

class Sesion(object):
    
    def __init__(self, pAlfabeto):
        self.alfabeto = pAlfabeto
        self.obligatorio = 3
        self.fichero = ""
        self.min = 0
        self.max = 0
        self.desde = ""
        
    def comprobacionArgumentos(self, argumentos):
        estado = True
        
        for i in range(0, len(argumentos)):
            argumento = argumentos[i].replace("-","").lower()
            
            if (argumento == "fichero"):
                self.fichero = argumentos[i+1]
                self.obligatorio -= 1
            elif (argumento == "min"):
                self.min = argumentos[i+1]
                self.obligatorio -= 1
            elif (argumento == "max"):
                self.max = argumentos[i+1]
                self.obligatorio -= 1
            elif (argumento == "desde"):
                self.desde = argumentos[i+1]
            elif (argumento == "help"):
                self.mostrarInformacion()
                return False   
        
        if (self.obligatorio > 0):
            estado = False
            print "Faltan argumentos obligatorios"
            self.mostrarInformacion()
        return estado
    
    def mostrarInformacion(self):
        print "Generador de diccionario v0.1"
        print "diccionario.py -fichero <fichero_salida> -min <longitud_minima> -max <longitud_maxima> [-desde <palabra_semilla>]"

    
    