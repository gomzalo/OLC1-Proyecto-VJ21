from Abstract.NodoAST import NodoAST
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo

class Declaracion(Instruccion):
    def __init__(self, identificador, tipo, fila, columna, expresion=None):
        self.identificador = identificador
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.arreglo = False

    def interpretar(self, tree, table):
        value = None
        
        # tipo = TIPO.NULO
        # tipoexp = None
        
        if self.expresion != None:
            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
            if isinstance(value, Excepcion): return value
            self.tipo = self.expresion.tipo

        # if self.tipo != self.expresion.tipo:
        #     return Excepcion("Semantico", "Tipo de dato diferente en Declaracion", self.fila, self.columna)

        simbolo = Simbolo(str(self.identificador), self.tipo, self.arreglo, self.fila, self.columna, value)
        # simbolo = Simbolo(str(self.identificador), TIPO.NULO, self.fila, self.columna, value)

        result = table.setTabla(simbolo)

        if isinstance(result, Excepcion): return result

        return None
    
    def getNodo(self):
        nodo = NodoAST("DECLARACION")
        # nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.identificador))
        # nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo