class Arbol:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.funciones = []
        self.excepciones = []
        self.consola = ""
        self.TSGlobal = None
        self.dot = ""
        self.contador = 0

    def getInstrucciones(self):
        return self.instrucciones

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def getExcepciones(self):
        return self.excepciones

    def setExcepciones(self, excepciones):
        self.excepciones = excepciones

    def getConsola(self):
        return self.consola

    def setConsola(self, consola):
        self.consola = consola

    def updateConsola(self, cadena):
        self.consola += str(cadena) + '\n'

    def getTSGlobal(self):
        return self.TSglobal

    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal

    def getFunciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None

    def addFuncion(self, funcion):
        self.funciones.append(funcion)
        
    def getDot(self, raiz): # Devuelve el string de la grafica en Graphviz
        self.dot = ""
        self.dot += "\n\tdigraph {\n"
        self.dot += "\n\t\tgraph[color = \"lightcyan:mistyrose\", fontcolor = \"darkslateblue\", fontname = serif, style = filled, label = \"Catedraticos\"];"
        self.dot += "\n\t\tnode[shape = egg, style = filled, color = \"gray9\", fillcolor = navyblue, fontcolor = white, peripheries = 2];"
        self.dot += "\n\t\tedge[color = \"deeppink:gray38:firebrick1\"];"
        self.dot += "\n"
        self.dot += "\n"
        self.dot += "\t\tn0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        self.contador = 1
        self.recorrerAST("n0", raiz)
        self.dot += "\t}"
        return self.dot
    
    def recorrerAST(self, id_padre, nodo_padre):
        for hijo in nodo_padre.getHijos():
            nombre_hijo = "n" + str(self.contador)
            self.dot += "\t\t" + nombre_hijo + "[label=\"" + hijo.getValor().replace("\"", "\\\"") + "\"];\n"
            self.dot += "\t\t" + id_padre + "->" + nombre_hijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombre_hijo, hijo)