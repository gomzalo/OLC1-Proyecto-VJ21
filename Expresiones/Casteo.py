from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorLogico

class Casteo(Instruccion):
    def __init__(self, tipo, expresion, fila, columna):
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        
    def interpretar(self, tree, table):
        val = self.expresion.interpretar(tree, table)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if self.tipo == TIPO.DECIMAL:
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     DOUBLE    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # :::::::::::::::::::::::::::::::::::      Combinaciones INT      :::::::::::::::::::::::::::::::::::
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Double.", self.fila, self.columna)
            # :::::::::::::::::::::::::::::::::::      Combinaciones CHARACTER      :::::::::::::::::::::::::::::::::::
            elif  self.expresion.tipo == TIPO.CHARACTER:
                try:
                    return float(ord(val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Double.", self.fila, self.columna)
            # :::::::::::::::::::::::::::::::::::      Combinaciones STRING      :::::::::::::::::::::::::::::::::::
            elif self.expresion.tipo == TIPO.CADENA:
                try:
                    return float(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Double.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo erroneo de casteo para Double.", self.fila, self.columna)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if self.tipo == TIPO.ENTERO:
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     INT    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # :::::::::::::::::::::::::::::::::::      Combinaciones DOUBLE      :::::::::::::::::::::::::::::::::::
            if self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Int.", self.fila, self.columna)
            # :::::::::::::::::::::::::::::::::::      Combinaciones STRING      :::::::::::::::::::::::::::::::::::
            elif  self.expresion.tipo == TIPO.CADENA:
                try:
                    return int(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Int.", self.fila, self.columna)
            # :::::::::::::::::::::::::::::::::::      Combinaciones CHARACTER      :::::::::::::::::::::::::::::::::::
            elif  self.expresion.tipo == TIPO.CHARACTER:
                try:
                    return int(ord(val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Int.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Int.", self.fila, self.columna)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if self.tipo == TIPO.CHARACTER:
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     CHARACTER    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # :::::::::::::::::::::::::::::::::::      Combinaciones INT      :::::::::::::::::::::::::::::::::::
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return chr(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Char.", self.fila, self.columna)
            # :::::::::::::::::::::::::::::::::::      Combinaciones DOUBLE      :::::::::::::::::::::::::::::::::::
            elif  self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return chr(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Char.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Char.", self.fila, self.columna)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if self.tipo == TIPO.CADENA:
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     STRING    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # :::::::::::::::::::::::::::::::::::      Combinaciones INT      :::::::::::::::::::::::::::::::::::
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para String.", self.fila, self.columna)
            # :::::::::::::::::::::::::::::::::::      Combinaciones DOUBLE      :::::::::::::::::::::::::::::::::::
            elif  self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para String.", self.fila, self.columna)
            # :::::::::::::::::::::::::::::::::::      Combinaciones BOOLEANO      :::::::::::::::::::::::::::::::::::
            elif  self.expresion.tipo == TIPO.BOOLEANO:
                try:
                    return str(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para String.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para String.", self.fila, self.columna)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if self.tipo == TIPO.BOOLEANO:
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~     BOOLEANO    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # :::::::::::::::::::::::::::::::::::      Combinaciones INT      :::::::::::::::::::::::::::::::::::
            if self.expresion.tipo == TIPO.ENTERO:
                try:
                    return bool(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Booleano.", self.fila, self.columna)
            # :::::::::::::::::::::::::::::::::::      Combinaciones DOUBLE      :::::::::::::::::::::::::::::::::::
            elif  self.expresion.tipo == TIPO.DECIMAL:
                try:
                    return bool(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Booleano.", self.fila, self.columna)
            # :::::::::::::::::::::::::::::::::::      Combinaciones STRING      :::::::::::::::::::::::::::::::::::
            elif  self.expresion.tipo == TIPO.CADENA:
                try:
                    return bool(self.obtenerVal(self.expresion.tipo, val))
                except:
                    return Excepcion("Semantico", "No se puede castear para Booleano.", self.fila, self.columna)
            return Excepcion("Semantico", "Tipo Erroneo de casteo para Booleano.", self.fila, self.columna)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def getNodo(self):
        nodo = NodoAST("CASTEO")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijoNodo(self.expresion.getNodo())
        return nodo

    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        elif tipo == TIPO.CHARACTER:
            return chr(val)
        return str(val)