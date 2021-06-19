'''
----------------------------------------------------
|   Universidad de San Carlos de Guatemala          |
|   Facultad de Ingenieria                          |
|   Escuela de Sistemas                             |
|   Laboratrio                                      |
|   Organización de lenguajes y compiladores 1      |
|   Proyecto - Vacaciones junio 2021                |
|   JPR                                             |
----------------------------------------------------
|   Gonzalo Antonio García Solares                  |
|   201318652                                       |
----------------------------------------------------
'''

# ********************************************************
# ******************       LEXICO      *******************
# ********************************************************
import re
from TS.Excepcion import Excepcion

errores = []

reservadas = {
    'int'       : 'RINT',
    'float'     : 'RFLOAT',
    'boolean'   : 'RBOOLEAN',
    'string'    : 'RSTRING',
    'print'     : 'RPRINT',
    'if'        : 'RIF',
    'else'      : 'RELSE',
    'while'     : 'RWHILE',
    'true'      : 'RTRUE',
    'false'     : 'RFALSE',
    'var'       : 'RVAR',
    'null'      : 'RNULL',
    'break'     : 'RBREAK',
    'continue'  : 'RCONTINUE',
    'main'      : 'RMAIN',
    'func'      : 'RFUNC'
}

tokens = [
    'PUNTOCOMA',
    'PARA',
    'PARC',
    'CORA',
    'CORC',
    'LLAVEA',
    'LLAVEC',
    'COMA',
    'MAS',
    'MENOS',
    'MASMAS',
    'MENOSMENOS',
    'POR',
    'DIV',
    'POT',
    'MOD',
    'MENORQUE',
    'MAYORQUE',
    'MENORIGUAL',
    'MAYORIGUAL',
    'IGUALIGUAL',
    'DIFERENTE',
    'IGUAL',
    'AND',
    'OR',
    'NOT',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'NULO',
    'ID'
] + list(reservadas.values())

# -------------     tokens      -------------

t_PARA          = r'\('
t_PARC          = r'\)'
t_CORA          = r'\['
t_CORC          = r'\]'
t_LLAVEA        = r'\{'
t_LLAVEC        = r'\}'
t_COMA          = r','
t_MAS           = r'\+'
t_MENOS         = r'-'
t_MASMAS        = r'\+\+'
t_MENOSMENOS    = r'--'
t_POR           = r'\*'
t_DIV           = r'/'
t_POT           = r'\*\*'
t_MOD           = r'%'
t_MENORQUE      = r'<'
t_MAYORQUE      = r'>'
t_MENORIGUAL    = r'<='
t_MAYORIGUAL    = r'>='
t_IGUALIGUAL    = r'=='
t_DIFERENTE     = r'=!'
t_IGUAL         = r'='
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_PUNTOCOMA     = r';'


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("El valor es demasiado grande '%d'" % t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor es demasiado grande '%d'" % t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value.lower(), 'ID')
    return t

def t_CADENA(t):
    r'(\".*(\\")*?\")'
    t.value = t.value[1:-1] # Removiendo comillas
    t.value = t.value.replace("\\", "") # Removiendo barra
    return t

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# -------------     Caracteres ignorados        -------------

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t): #LEXICOS
    errores.append(Excepcion("Lexico", "Error léxico." + t.value[0], t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Obtener columna
#   input: Entrada de texto
#   token: Instancia del token
def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador lexico
import ply.lex as lex
lexer = lex.lex(reflags= re.IGNORECASE)

# Asociacion de operadores y precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'UNOT'),
    ('left', 'MAYORIGUAL', 'MAYORQUE', 'MENORIGUAL', 'MENORQUE', 'DIFERENTE', 'IGUALIGUAL'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MOD', 'POR', 'DIV'),
    ('nonassoc', 'POT'),
    ('right', 'UMENOS'),
    ('right', 'UMASMAS'),
    ('right', 'UMENOSMENOS'),
)

# ********************************************************
# ****************       SINTACTICO      *****************
# ********************************************************
#Abstract
from Abstract.Instruccion import Instruccion
from Instrucciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import OperadorAritmetico, TIPO, OperadorRelacional, OperadorLogico
from Expresiones.Aritmetica import Aritmetica
from Expresiones.Relacional import Relacional
from Expresiones.Logica import Logica
from Instrucciones.Declaracion import Declaracion
from Expresiones.Identificador import Identificador
from Instrucciones.Asignacion import Asignacion
from Instrucciones.If import If
from Instrucciones.While import While
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Main import Main
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamada import Llamada
from Instrucciones.Incremento import Incremento
from Instrucciones.Decremento import Decremento

# -------------     Definicion de la gramatica      -------------

def p_init(t):
    'init               : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t):
    'instrucciones      : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]

#///////////////////////////////////////INSTRUCCIONES//////////////////////////////////////////////////

def p_instrucciones_instruccion(t):
    'instrucciones      : instruccion'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]
#///////////////////////////////////////PUNTO COMA//////////////////////////////////////////////////

def p_terminacion(t):
    '''terminacion        : PUNTOCOMA
                          |
    '''
    t[0] = None
#///////////////////////////////////////INSTRUCCION//////////////////////////////////////////////////

def p_instruccion(t):
    '''instruccion      : imprimir_instr terminacion
                        | declaracion_instr terminacion
                        | asignacion_instr terminacion
                        | if_instr
                        | while_instr
                        | break_instr terminacion
                        | continue_instr terminacion
                        | main_instr
                        | funcion_instr
                        | llamada_instr terminacion
                        | incremento_instr terminacion
                        | decremento_instr terminacion
                        '''
    t[0] = t[1]

def p_instruccion_error(t):
    'instruccion        : error terminacion'
    errores.append(Excepcion("Sintáctico","Error Sintáctico." + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""

#///////////////////////////////////////IMPRIMIR//////////////////////////////////////////////////

def p_imprimir(t):
    'imprimir_instr     : RPRINT PARA expresion PARC'
    t[0] = Imprimir(t[3], t.lineno(1), find_column(input, t.slice[1]))
#///////////////////////////////////////DECLARACION//////////////////////////////////////////////////

def p_declaracion(t) :
    'declaracion_instr     : RVAR ID IGUAL expresion'
    t[0] = Declaracion(t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])
    # t[0] = Declaracion(t[1], t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])

#///////////////////////////////////////ASIGNACION//////////////////////////////////////////////////

def p_asignacion(t) :
    'asignacion_instr     : ID IGUAL expresion'
    t[0] = Asignacion(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////INCREMENTO//////////////////////////////////////////////////

def p_incremento(t) :
    'incremento_instr     : ID MASMAS'
    t[0] = Incremento(t[1], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////DECREMENTO//////////////////////////////////////////////////

def p_decremento(t) :
    'decremento_instr     : ID MENOSMENOS'
    t[0] = Decremento(t[1], t.lineno(1), find_column(input, t.slice[1]))


#///////////////////////////////////////IF//////////////////////////////////////////////////

def p_if1(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_if2(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_if3(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr'
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))
#///////////////////////////////////////WHILE//////////////////////////////////////////////////

def p_while(t) :
    'while_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = While(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////BREAK//////////////////////////////////////////////////

def p_break(t) :
    'break_instr     : RBREAK'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////CONTINUE//////////////////////////////////////////////////

def p_continue(t) :
    'continue_instr     : RCONTINUE'
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////MAIN//////////////////////////////////////////////////

def p_main(t) :
    'main_instr     : RMAIN PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Main(t[5], t.lineno(1), find_column(input, t.slice[1]))


#///////////////////////////////////////FUNCION//////////////////////////////////////////////////

def p_funcion(t) :
    'funcion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////

def p_llamada(t) :
    'llamada_instr     : ID PARA PARC'
    t[0] = Llamada(t[1], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////TIPO//////////////////////////////////////////////////

def p_tipo(t) :
    '''tipo     : RINT
                | RFLOAT
                | RSTRING
                | RBOOLEAN
                 '''
    if t[1] == 'int':
        t[0] = TIPO.ENTERO
    elif t[1] == 'float':
        t[0] = TIPO.DECIMAL
    elif t[1] == 'string':
        t[0] = TIPO.CADENA
    elif t[1] == 'boolean':
        t[0] = TIPO.BOOLEANO

#///////////////////////////////////////EXPRESION//////////////////////////////////////////////////

def p_expresion_binaria(t):
    '''
    expresion           : expresion MAS expresion
                        | expresion MENOS expresion
                        | expresion MENORQUE expresion
                        | expresion MAYORQUE expresion
                        | expresion MENORIGUAL expresion
                        | expresion MAYORIGUAL expresion
                        | expresion IGUALIGUAL expresion
                        | expresion DIFERENTE expresion
                        | expresion AND expresion
                        | expresion OR expresion
    '''

    if t[2] == '+':
        t[0] = Aritmetica(OperadorAritmetico.MAS, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '-':
        t[0] = Aritmetica(OperadorAritmetico.MENOS, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '<':
        t[0] = Relacional(OperadorRelacional.MENORQUE, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '>':
        t[0] = Relacional(OperadorRelacional.MAYORQUE, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '<=':
        t[0] = Relacional(OperadorRelacional.MENORIGUAL, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '>=':
        t[0] = Relacional(OperadorRelacional.MAYORIGUAL, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '==':
        t[0] = Relacional(OperadorRelacional.IGUALIGUAL, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '=!':
        t[0] = Relacional(OperadorRelacional.DIFERENTE, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '&&':
        t[0] = Logica(OperadorLogico.AND, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(OperadorLogico.OR, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))

def p_expresion_unaria(t):
    '''
    expresion           : MENOS expresion %prec UMENOS
                        | NOT expresion %prec UNOT
                        | expresion MENOSMENOS %prec UMENOSMENOS
                        | expresion MASMAS %prec UMASMAS
    '''

    if t[1] == '-':
        t[0] = Aritmetica(OperadorAritmetico.UMENOS, t[2], None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logica(OperadorLogico.NOT, t[2], None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '++':
        t[0] = Aritmetica(OperadorAritmetico.MASMAS, t[1], None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '--':
        t[0] = Aritmetica(OperadorAritmetico.MENOSMENOS, t[1], None, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_agrupacion(t):
    '''
    expresion           : PARA expresion PARC
    '''
    t[0] = t[2]

def p_expresion_identificador(t):
    '''expresion        : ID'''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_entero(t):
    '''expresion        : ENTERO'''
    t[0] = Primitivos(TIPO.ENTERO, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_decimal(t):
    '''expresion        : DECIMAL'''
    t[0] = Primitivos(TIPO.DECIMAL, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_cadena(t):
    '''expresion        : CADENA'''
    t[0] = Primitivos(TIPO.CADENA, str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_true(t):
    '''expresion : RTRUE'''
    t[0] = Primitivos(TIPO.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_false(t):
    '''expresion : RFALSE'''
    t[0] = Primitivos(TIPO.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))

import ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores

def parse(inp):
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex(reflags=re.IGNORECASE)
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

# INTERFAZ

f = open("./entrada.txt", "r")
entrada = f.read()

from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos

instrucciones = parse(entrada.lower()) # ARBOL AST
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolos()
ast.setTSglobal(TSGlobal)
for error in errores:                   # CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
    ast.getExcepciones().append(error)
    ast.updateConsola(error.toString())

for instruccion in ast.getInstrucciones():      # 1RA PASADA (Declaraciones y asignaciones)
    if isinstance(instruccion, Funcion):
        ast.addFuncion(instruccion)  # GUARDAR LA FUNCION EN "MEMORIA" (EN EL ARBOL)
    if isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion):
        value = instruccion.interpretar(ast,TSGlobal)
        if isinstance(value, Excepcion) :
            ast.getExcepciones().append(value)
            ast.updateConsola(value.toString())
        if isinstance(value, Break):
            err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())

for instruccion in ast.getInstrucciones():      # 2DA PASADA (Main)
    contador = 0
    if isinstance(instruccion, Main):
        contador += 1
        if contador == 2:   # Verificando la duplicidad
            err = Excepcion("Semantico", "Se encontraron 2 funciones Main.", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())
            break
        value = instruccion.interpretar(ast, TSGlobal)
        if isinstance(value, Excepcion):
            ast.getExcepciones().append(value)
            ast.updateConsola(value.toString())
        if isinstance(value, Break):
            err = Excepcion("Semantico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())

for instruccion in ast.getInstrucciones():    # 3ERA PASADA (SENTENCIAS FUERA DE MAIN)
    if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion)):
        err = Excepcion("Semantico", "¡Sentencias fuera de función Main!", instruccion.fila, instruccion.columna)
        ast.getExcepciones().append(err)
        ast.updateConsola(err.toString())

print(ast.getConsola())