from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue

class Switch(Instruccion):
    def __init__(self, condicion, instruccionesSwCsDf, instruccionesSwCs, instruccionesSwDf, fila, columna):
        self.condicion = condicion
        self.instruccionesSwCsDf = instruccionesSwCsDf
        self.instruccionesSwCs = instruccionesSwCs
        self.instruccionesSwDf = instruccionesSwDf
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree, table)
        if isinstance(condicion, Excepcion): return condicion
        print("Int SW")
        if self.condicion.tipo != None: # Verificando si es uan condicion valida
            # SW - CA - DEF
            print("SW NO NULL")
            if self.instruccionesSwCsDf != None and self.instruccionesSwCs == None and self.instruccionesSwDf != None:
                nuevaTabla = TablaSimbolos(table)    # Nuevo entorno SWITCH
                print("CASO1")
                for cond_instruccion in self.instruccionesSwCsDf:
                    tabla_case = TablaSimbolos(nuevaTabla) # Nuevo entorno CASE
                    # result_case = cond_instruccion.interpretar(tree, tabla_case)  # Ejecuta instruccion dentro de switch
                    result_case = cond_instruccion.condicion.valor  # Ejecuta instruccion dentro de switch
                    print("RESCAS1", result_case)
                    if isinstance(result_case, Excepcion):
                        tree.getExcepciones().append(result_case)
                        tree.updateConsola(result_case.toString())
                    if isinstance(result_case, Break): return result_case
                    if isinstance(result_case, Continue): return result_case
                    # print("RESULT CASE VALOR: ", str(result_case))
                    if result_case == condicion:
                        print("SW COMP", result_case == condicion)
                        for instruccion in cond_instruccion.instrucciones:
                            result = instruccion.interpretar(tree, nuevaTabla)  # Ejecuta instruccion dentro de cases
                            if isinstance(result, Excepcion):
                                tree.getExcepciones().append(result)
                                tree.updateConsola(result.toString())
                            if isinstance(result, Break): return result
                            if isinstance(result, Continue): return result
                for cond_instr in self.instruccionesSwDf:
                    tabla_default = TablaSimbolos(nuevaTabla)   # Nuevo entorno DEFAULT
                    result_default = cond_instr.interpretar(tree, tabla_default) # Ejecuta instruccion dentro default
                    if isinstance(result_default, Excepcion):
                        tree.getExcepciones().append(result_default)
                        tree.updateConsola(result_default.toString())
                    if isinstance(result_default, Break): return result_default
                    if isinstance(result_default, Continue): return result_default
            # SW - CA
            elif self.instruccionesSwCsDf == None and self.instruccionesSwCs != None and self.instruccionesSwDf == None:
                nuevaTabla = TablaSimbolos(table)    # Nuevo entorno SWITCH
                print("CASO2")
                for cond_instruccion in self.instruccionesSwCs:
                    tabla_case = TablaSimbolos(nuevaTabla) # Nuevo entorno CASE
                    result_case = cond_instruccion.condicion.valor  # Ejecuta instruccion dentro de switch
                    if isinstance(result_case, Excepcion):
                        tree.getExcepciones().append(result_case)
                        tree.updateConsola(result_case.toString())
                    if isinstance(result_case, Break): return result_case
                    if isinstance(result_case, Continue): return result_case
                    if result_case == condicion:
                        for instruccion in cond_instruccion.instrucciones:
                            result = instruccion.interpretar(tree, nuevaTabla)  # Ejecuta instruccion dentro de cases
                            if isinstance(result, Excepcion):
                                tree.getExcepciones().append(result)
                                tree.updateConsola(result.toString())
                            if isinstance(result, Break): return result
                            if isinstance(result, Continue): return result
                # SW - DF
            elif self.instruccionesSwCsDf == None and self.instruccionesSwCs == None and  self.instruccionesSwDf != None:
                nuevaTabla = TablaSimbolos(table)   # Nuevo entorno SWITCH
                print("CASO3")
                for instruccion in self.instruccionesSwDf:
                    # tabla_default = TablaSimbolos(nuevaTabla)   # Nuevo entorno DEFAULT
                    # print("INSTCASO3: ", instruccion)
                    result_default = instruccion.interpretar(tree, nuevaTabla) # Ejecuta instruccion dentro default
                    if isinstance(result_default, Excepcion):
                        tree.getExcepciones().append(result_default)
                        tree.updateConsola(result_default.toString())
                    if isinstance(result_default, Break): return result_default
                    if isinstance(result_default, Continue): return result_default
        else:
            return Excepcion("Semantico", "Tipo de dato no booleano en SW.", self.fila, self.columna)