from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break

class Funcion(Instruccion):
    def __init__(self, nombre, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        nuevaTabla = TablaSimbolos(table)
        for insttruccion in self.instrucciones: # Realizar las acciones
            value = insttruccion.interpretar(tree, nuevaTabla)
            if isinstance(value, Excepcion):
                tree.getExcepciones().append(value)
                tree.updateConsola(value.toString())
            if isinstance(value, Break):
                err = Excepcion("Semantico", "Sentencia \"Break\" fuera de ciclo.", insttruccion.fila, insttruccion.columna)
                tree.getExcepciones().append(err)
                tree.updateConsola(err.toString())
        return None