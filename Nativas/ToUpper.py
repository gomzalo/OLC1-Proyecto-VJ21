from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class ToUpper(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
        
    def interpretar(self, tree, table):
        simbolo = table.getTabla("toUpper##Param1")
        print("valor: " + str(simbolo.getValor()))
        print("tipo: " + str(simbolo.getTipo()))
        
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de ToUpper.", self.fila, self.columna)
        # print(simbolo.getTipo())
        if simbolo.getTipo() != TIPO.CADENA:
            return Excepcion("Semantico", "Tipo de parámetro de ToUpper, no es una cadena.", self.fila, self.columna)
        else:        
            self.tipo = simbolo.getTipo()
            return simbolo.getValor().upper()