from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Incremento import Incremento
from Instrucciones.Decremento import Decremento
from Instrucciones.Asignacion import Asignacion
from Instrucciones.Declaracion import Declaracion

class For(Instruccion):
    def __init__(self, declaracion_asignacion, condicion, actualizacion, instrucciones, fila, columna):
        self.declaracion_asignacion = declaracion_asignacion
        self.condicion = condicion
        self.actualizacion = actualizacion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        # Asignacion o declaracion
        declaracion_asignacion = self.declaracion_asignacion.interpretar(tree, table)
        if isinstance(declaracion_asignacion, Excepcion): return declaracion_asignacion
        
        while True:
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Excepcion): return condicion

            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:     # Verifica si la condicion es verdadera
                    nuevaTabla = TablaSimbolos(table)   # Nuevo entorno
                    for instruccion in self.instrucciones:
                        if isinstance(instruccion, Declaracion) and instruccion.identificador == self.actualizacion.identificador:
                            err = Excepcion("Semantico", "Ya existe una variable con el mismo nombre en este contexto.", instruccion.fila, instruccion.columna)
                            tree.getExcepciones().append(err)
                            tree.updateConsola(err.toString())
                            return None
                        result = instruccion.interpretar(tree, nuevaTabla)  # Ejecuta instruccion dentro del if (For?)
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                        if isinstance(result, Continue): return None
                    # Actualizacion (Asignacion | Incremento | Decremento)
                    actualizacion = self.actualizacion.interpretar(tree, table)
                    if isinstance(actualizacion, Excepcion): return actualizacion
        
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)