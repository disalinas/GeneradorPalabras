# coding: utf-8
'''
Created on 10/12/2012

@author: ikarus
'''

class Generador(object):

    def __init__(self, pFichero, pAlfabeto, pLonMin, pLonMax, pInicializar):
        self.combinaciones = []
        self.fichero = str(pFichero)
        self.alfabeto = pAlfabeto
        self.lonMin = int(pLonMin)
        self.lonMax = int(pLonMax)
        self.inicializar = pInicializar

    ''' Dado un alfabeto se encarga de generar sub-alfabetos de distintas longitudes. '''
    ''' Precondicion: La funcion recibe el alfabeto con las letras a ser utilizadas, un numero que indica '''
    ''' la longitud minima de las palabras resultantes y otro numero que indica la longitud maxima de las '''
    ''' palabras que se obtendran. '''
    def getCombinaciones(self):        
        siguientePalabra = self.primeraPalabra(self.inicializar)
        if (len(siguientePalabra) > 0):
            self.lonMin = len(siguientePalabra)
        if (len(siguientePalabra) <= self.lonMax):
            diccionario = open(self.fichero,"w")
            for i in range(self.lonMin,self.lonMax+1):
                self.getCombinacion(diccionario, self.combinaciones, self.alfabeto, i, siguientePalabra.pop() if (len(siguientePalabra) > 0) else "-")
            diccionario.close()
        else:
            print "La siguiente palabra a la palabra semilla (" + ''.join(self.inicializar) + ") está fuera del rango."
        return self.combinaciones
    
    def primeraPalabra(self, palabra):
        lista = []
        if (len(palabra) > 0):
            for letra in palabra:
                lista.append(letra)
            sigPalabra = self.siguientePalabra(lista)
            lista = sigPalabra[::-1]
        return lista
    
    def siguientePalabra(self, palabra):
        nuevaPalabra = []
        ultima = palabra.pop()
        if (ultima == self.alfabeto[len(self.alfabeto)-1]):
            if (len(palabra) > 0):
                nuevaPalabra = self.siguientePalabra(palabra)
                nuevaPalabra.append(self.alfabeto[0])
            else:
                nuevaPalabra.append(self.alfabeto[0])
                nuevaPalabra.append(self.alfabeto[0])
        else:
            letra = self.alfabeto[self.alfabeto.index(ultima) + 1]
            palabra.append(letra)
            nuevaPalabra = palabra
        return nuevaPalabra
    
    def getCombinacion(self, diccionario, combinaciones, alfabeto, longitud, aux, palabra = ''):
        if (longitud > 0):
            for letra in alfabeto:
                if (aux == "-"):
                    self.getCombinacion(diccionario, combinaciones, alfabeto, longitud-1, aux, palabra + letra)
                else:
                    if (letra == aux):
                        aux = "-"
                        self.getCombinacion(diccionario, combinaciones, alfabeto, longitud-1, aux, palabra + letra)
        else:
            diccionario.write(palabra + "\")
            print "Actual:" + palabra

        ''' Funcion encargada de obtener todas las posibles permutaciones sin repeticion dado un alfabeto '''
        ''' Postcondicion: Devuelve un array con las permutaciones sin repeticion posibles. En caso de '''
        ''' no haber palabras, devuelve un array vacio. '''
        def getPermutaciones(self, alfabeto):
            permutaciones = []
            for letra in alfabeto:
                lista = list(alfabeto)        
                lista.remove(letra)        
                devolucion = getPermutaciones(lista)
        
            if len(devolucion) > 0:
                for permutacion in devolucion:
                    if (not self.existePalabra(letra + permutacion, permutaciones)):
                        permutaciones.append(letra + permutacion)
            else:
                if (not self.existePalabra(letra, permutaciones)):
                    permutaciones.append(letra)
            return permutaciones

        ''' Dado una palabra y un array de palabras (permutaciones) verifica si la palabra ya existe en '''
        ''' el array de palabras. '''
        ''' Postcondicion: Devuelve True si la palabra existe en el array de palabras. False en otro caso. '''
        def existePalabra(self, palabra, permutaciones):
            existe = False
            for pal in permutaciones:
                if (palabra.lower() == pal.lower()):
                    existe = True
                    break
            return existe
        
