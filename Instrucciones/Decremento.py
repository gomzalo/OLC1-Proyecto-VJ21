from Abstract.NodoAST import NodoAST
from TS.Tipo import TIPO
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo

class Decremento(Instruccion):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.arreglo = False

    def interpretar(self, tree, table):
        value = None # Valor a asignar a la variable
        # if isinstance(value, Excepcion): return value
        new_symbol = table.getTabla(self.identificador)
        
        if new_symbol == None:
            return Excepcion("Semantico", "Variable no encontrada.", self.fila, self.columna)
        if new_symbol.tipo == TIPO.NULO:
            return Excepcion("Semantico", "Tipo de dato no incrementable.", self.fila, self.columna)
        
        if new_symbol.tipo == TIPO.ENTERO or new_symbol.tipo == TIPO.DECIMAL:
            value = new_symbol.getValor()
            if isinstance(value, Excepcion):
                return value
            value = value - 1
            
            simbolo = Simbolo(str(self.identificador), new_symbol.tipo, self.arreglo, self.fila, self.columna, value)

            result = table.actualizarTabla(simbolo)
            
            if isinstance(result, Excepcion): return result
            return value
        else:
            return Excepcion("Semantico", "Tipo de dato no incrementable.", self.fila, self.columna)
        return None
    
    def getNodo(self):
        nodo = NodoAST("DECREMENTO")
        nodo.agregarHijo(str(self.identificador))
        # nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo