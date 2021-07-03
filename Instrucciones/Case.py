from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
# from Instrucciones.Return import Return

class Case(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree, table)
        print("CASE VALOR COND", condicion)
        if isinstance(condicion, Excepcion): return condicion

        if self.condicion.tipo != TIPO.NULO:
            # if bool(condicion) == True:     # Verificando si es verdadera la condicion
                nuevaTabla = TablaSimbolos(table)    # Nuevo entorno
                # for instruccion in self.instrucciones:
                #     result = instruccion.interpretar(tree, nuevaTabla)  # Ejecuta instruccion dentro del If
                #     print("CASE VALOR EXP", result)
                    # if isinstance(result, Excepcion):
                    #     tree.getExcepciones().append(result)
                    #     tree.updateConsola(result.toString())
                    # if isinstance(result, Break): return result
                    # # if isinstance(result, Return): return result
                    # if isinstance(result, Continue): return Continue
                # return result
        else:
            return Excepcion("Semantico", "Dato nulo en CASE.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("CASE")
        nodo.agregarHijo(str(self.condicion))
        nodo.agregarHijo(str(self.instrucciones))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo