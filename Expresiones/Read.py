# from Abstract.NodoAST import NodoAST
from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA
        
    def interpretar(self, tree, table):
        print(tree.getConsola()) # Imprime consola
        print("Ingreso a READ.\nIngrese un valor: ")
        tree.setConsola("") # Reset consola
        # Ejemplo
        lectura = input() # Obteniendo valor ingresado
        return lectura
    
    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo
        