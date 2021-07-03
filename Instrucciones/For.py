from Abstract.NodoAST import NodoAST
from Instrucciones.Return import Return
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
        if isinstance(self.declaracion_asignacion, Asignacion):
            cond = self.declaracion_asignacion.interpretar(tree, table)
            if isinstance(cond, Excepcion): return cond
        
        # Asignacion o declaracion
        tabla_intermedia = TablaSimbolos(table);
        cond = self.declaracion_asignacion.interpretar(tree, tabla_intermedia)
        if isinstance(cond, Excepcion): return cond
        
        while True:
            cond_ = self.condicion.interpretar(tree, tabla_intermedia)
            if isinstance(cond_, Excepcion): return cond_

            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(cond_) == True:     # Verifica si la condicion es verdadera
                    nuevaTabla = TablaSimbolos(tabla_intermedia)   # Nuevo entorno
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla)  # Ejecuta instruccion dentro del if (For?)
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                        if isinstance(result, Continue): break
                        if isinstance(result, Return): return result
                    # Actualizacion (Asignacion | Incremento | Decremento)
                    actualizacion = self.actualizacion.interpretar(tree, tabla_intermedia)
                    if isinstance(actualizacion, Excepcion): return actualizacion
        
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de dato no booleano en FOR.", self.fila, self.columna)
            
    def getNodo(self):
        nodo = NodoAST("FOR")

        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo