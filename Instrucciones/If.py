from Instrucciones.Return import Return
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue

class If(Instruccion):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.elseIf = ElseIf
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree, table)
        if isinstance(condicion, Excepcion): return condicion

        if self.condicion.tipo == TIPO.BOOLEANO:
            if bool(condicion) == True:     # Verificando si es verdadera la condicion
                nuevaTabla = TablaSimbolos(table)    # Nuevo entorno
                for instruccion in self.instruccionesIf:
                    result = instruccion.interpretar(tree, nuevaTabla)  # Ejecuta instruccion dentro del If
                    if isinstance(result, Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    if isinstance(result, Break): return result
                    if isinstance(result, Continue): break
                    if isinstance(result, Return): return result
            else:       # Else
                if self.instruccionesElse != None:
                    nuevaTabla = TablaSimbolos(table)   # Nuevo entorno
                    for instruccion in self.instruccionesElse:
                        result = instruccion.interpretar(tree, nuevaTabla)  # Ejectura instrucciones dentro del if (else?)
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return result
                        if isinstance(result, Continue): break
                        if isinstance(result, Return): return result
                elif self.elseIf != None:
                    result = self.elseIf.interpretar(tree, table)
                    if isinstance(result, Excepcion): return result
                    if isinstance(result, Break): return result
                    if isinstance(result, Continue): return result
                    if isinstance(result, Return): return result

        else:
            return Excepcion("Semantico", "Tipo de dato no booleano en IF.", self.fila, self.columna)