import math
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO
from Instrucciones.Funcion import Funcion

class Round(Funcion):
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.NULO
        
    def interpretar(self, tree, table):
        simbolo = table.getTabla("round##Param1")
        
        if simbolo == None : return Excepcion("Semantico", "No se encontró el parámetro de Round.", self.fila, self.columna)
        # print(simbolo.getTipo())
        if simbolo.getTipo() != TIPO.DECIMAL:
            return Excepcion("Semantico", "Tipo de parámetro de Round, no es una cadena.", self.fila, self.columna)
        else:        
            self.tipo = simbolo.getTipo()
            val_original = simbolo.getValor()
            val_dec_str = str(val_original).split('.')[1]
            val_dec_str = val_dec_str[0:2]
            if len(val_dec_str) == 1:
                val_dec_str += "0"
            val_ent_str = str(val_original).split('.')[0]
            val_dec = int(val_dec_str)            
            val_ent = int(val_ent_str)
            # print("val_dec: " +  val_dec_str)
            # print("val_ent: " +  val_ent_str)
            if int(val_dec) >= 50: return val_ent + 1
            else: return val_ent
                
                