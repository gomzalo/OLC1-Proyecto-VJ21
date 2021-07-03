import math
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class Truncate(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
        
    def interpretar(self, tree, table):
        simbolo = table.getTabla("truncate##Param1")
        if simbolo == None : return Excepcion("Semantico", "No se encontró el valor de truncate.", self.fila, self.columna)
        
        if simbolo.getTipo() != TIPO.DECIMAL:
            return Excepcion("Semantico", "Tipo del valor de truncate, no es valido.", self.fila, self.columna)
        # if simbolo.getTipo() != TIPO.ENTERO:
        #     return Excepcion("Semantico", "Tipo del valor de truncate, no es valido.", self.fila, self.columna)
        # if simbolo.getTipo() == TIPO.ENTERO:
        #     try:
        #         simbolo.setValor(float(simbolo.getValor()))
        #         print("Entero papa: " + simbolo.getValor())
        #         simbolo.setTipo(TIPO.DECIMAL)
        #     except print(0):
        #         return Excepcion("Semantico", "No se puede convertir entero.", self.fila, self.columna)
        #         # pass
                
        
        self.tipo = simbolo.getTipo()
        return round(simbolo.getValor())