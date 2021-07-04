from Abstract.NodoAST import NodoAST
from TS.Simbolo import Simbolo
from Instrucciones.Funcion import Funcion
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break
from TS.Tipo import TIPO


class Llamada(Instruccion):
    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
        self.arreglo = False

    def interpretar(self, tree, table):
        result = tree.getFuncion(self.nombre.lower())  ## OBTENER LA FUNCION
        if result == None:  # NO SE ENCONTRO LA FUNCION
            return Excepcion("Semantico", "NO SE ENCONTRO LA FUNCION: " + self.nombre, self.fila, self.columna)
        nuevaTabla = TablaSimbolos(tree.getTSGlobal())
        # OBTENER PARAMETROS
        if len(result.parametros) == len(self.parametros): # LA CANTIDAD DE PARAMETROS ES LA ADECUADA
            contador = 0
            for expresion in self.parametros: # Se obtiene el valor del parametro en la llamada
                resultExpresion = expresion.interpretar(tree, table)
                if isinstance(resultExpresion, Excepcion): return resultExpresion
                # print("Tipo en llamada: " + str(expresion.tipo))
                    # ::::::::::::   Verificando si son nativas     ::::::::::::
                    # if str(result.parametros[contador]['identificador']) == "typeof##Param1":
                    #     print("Entro a nativa :v")
                    #     simbolo = Simbolo(str(result.parametros[contador]['identificador']).lower(), self.arreglo, expresion.tipo, self.fila, self.columna, resultExpresion)
                    #     # print(simbolo.getID())                        
                    #     resultTabla = nuevaTabla.setTabla(simbolo)
                    #     if isinstance(resultTabla, Excepcion): return resultTabla
                    # elif str(result.parametros[contador]['identificador']) == "toUpper##Param1":
                    #     print("Entro a nativa :v")
                    #     simbolo = Simbolo(str(result.parametros[contador]['identificador']).lower(), self.arreglo, expresion.tipo, self.fila, self.columna, resultExpresion)
                    #     # print(simbolo.getID())                        
                    #     resultTabla = nuevaTabla.setTabla(simbolo)
                    #     # if expresion.tipo != TIPO.CADENA:
                    #     #     return Excepcion("Semantico", "Tipo de parámetro de ToUpper, no es una cadena.", self.fila, self.columna)
                    #     if isinstance(resultTabla, Excepcion): return resultTabla
                # # ::::::::::::   Funciones normales     ::::::::::::
                # else:
                if result.parametros[contador]["tipo"] == expresion.tipo or result.parametros[contador]["tipo"] == TIPO.ANY: # Verificacion de tipo
                    # Creacion de simbolo e ingresarlo a la tabla de simbolos
                    if result.parametros[contador]["tipo"] == TIPO.ANY:
                        simbolo = Simbolo(str(result.parametros[contador]['identificador']).lower(), expresion.tipo, self.arreglo, self.fila, self.columna, resultExpresion)
                    else:
                        simbolo = Simbolo(str(result.parametros[contador]['identificador']).lower(), result.parametros[contador]['tipo'], self.arreglo, self.fila, self.columna, resultExpresion)
                    # print(simbolo.getID())                        
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Excepcion): return resultTabla
                    
                else:
                    return Excepcion("Semantico", "Tipo de dato diferente en parametros de la llamada.", self.fila, self.columna)
                
                contador += 1
                
        else:
            return Excepcion("Semantico", "Cantidad de Parametros incorrecta.", self.fila, self.columna)
        
        value = result.interpretar(tree, nuevaTabla)  # INTERPRETAR EL NODO FUNCION
        if isinstance(value, Excepcion): return value
        self.tipo = result.tipo

        return value
    
    def getNodo(self):
        nodo = NodoAST("LLAMADA A FUNCION")
        nodo.agregarHijo(str(self.nombre))
        parametros = NodoAST("PARAMETROS")
        for param in self.parametros:
            parametros.agregarHijoNodo(param.getNodo())
        nodo.agregarHijoNodo(parametros)
        return nodo