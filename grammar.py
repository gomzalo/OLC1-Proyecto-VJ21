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
    'for'       : 'RFOR',
    'true'      : 'RTRUE',
    'false'     : 'RFALSE',
    'var'       : 'RVAR',
    'null'      : 'RNULL',
    'break'     : 'RBREAK',
    'continue'  : 'RCONTINUE',
    'switch'    : 'RSWITCH',
    'case'      : 'RCASE',
    'default'   : 'RDEFAULT',
    'main'      : 'RMAIN',
    'func'      : 'RFUNC'
}

tokens = [
    'PUNTOCOMA',
    'DOSPUNTOS',
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
    'CHAR',
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
t_DOSPUNTOS     = r':'


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
    r'\"(\\[nN]|\\\"|\\\'|\\[tT]|\\[rR]|\\\\|\\\*|[^\\\'\"])*?\"'
    t.value = t.value[1:-1] # Removiendo comillas
    # t.value = t.value.replace('á', 'a')
    # t.value = t.value.replace('é', 'e')
    # t.value = t.value.replace('í', 'i')
    # t.value = t.value.replace('ó', 'o')
    # t.value = t.value.replace('ú', 'u')
    t.value = t.value.replace('\\r', '\r')# Removiendo barra
    t.value = t.value.replace('\\R', '\r')# Removiendo barra
    t.value = t.value.replace('\\t', '\t')# Removiendo barra
    t.value = t.value.replace('\\T', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\N', '\n')    
    t.value = t.value.replace("\\\'", "\'")
    t.value = t.value.replace("\\\"", "\"")
    t.value = t.value.replace('\\\\', '\\')
    return t

def t_CHAR(t):
    r'\'(\\[nN]|\\\"|\\\'|\\[tT]|\\\\|\\\*|[^\\\"\'])?\''
    t.value = t.value[1:-1]  # removiendo comillas
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\T', '\t')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\N', '\n')   
    t.value = t.value.replace("\\\'", "\'")
    t.value = t.value.replace("\\\"", "\"")
    t.value = t.value.replace('\\\\', '\\')
    return t

# Comentario simple // ...
def t_COMENTARIO_SIMPLE(t):
    r'\#[^\*].*\n'
    t.lexer.lineno += 1

def t_COMENTARIO_MULTILINEA(t):
    r'\#\*(.|\n)*?\*\#'
    t.lexer.lineno += t.value.count('\n')

# -------------     Caracteres ignorados        -------------

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t): #LEXICOS
    errores.append(Excepcion("Lexico", "Error léxico: " + t.value[0], t.lexer.lineno, find_column(input, t)))
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
    ('right', 'UMASMAS'),
    ('right', 'UMENOSMENOS'),
    ('right', 'UMENOS'),
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
from Instrucciones.For import For
from Instrucciones.Break import Break
from Instrucciones.Continue import Continue
from Instrucciones.Main import Main
from Instrucciones.Funcion import Funcion
from Instrucciones.Llamada import Llamada
from Instrucciones.Incremento import Incremento
from Instrucciones.Decremento import Decremento
from Instrucciones.Switch import Switch
from Instrucciones.Case import Case

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
                        | switch_instr
                        | while_instr
                        | for_instr
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
    # t[0] = Declaracion(t[2], TIPO.NULO, t.lineno(2), find_column(input, t.slice[2]), t[4])
    t[0] = Declaracion(t[2], t.lineno(2), find_column(input, t.slice[2]), t[4])
    
def p_declaracion_1(t) :
    'declaracion_instr     : RVAR ID'
    # t[0] = Declaracion(t[2], TIPO.NULO, t.lineno(2), find_column(input, t.slice[2]), None)
    t[0] = Declaracion(t[2], t.lineno(2), find_column(input, t.slice[2]), None)

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

def p_if_1(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], None, None, t.lineno(1), find_column(input, t.slice[1]))

def p_if_2(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE LLAVEA instrucciones LLAVEC'
    t[0] = If(t[3], t[6], t[10], None, t.lineno(1), find_column(input, t.slice[1]))

def p_if_3(t) :
    'if_instr     : RIF PARA expresion PARC LLAVEA instrucciones LLAVEC RELSE if_instr'
    t[0] = If(t[3], t[6], None, t[9], t.lineno(1), find_column(input, t.slice[1]))
    
#///////////////////////////////////////SWITCH//////////////////////////////////////////////////

def p_switch_1(t) :
    'switch_instr     : RSWITCH PARA expresion PARC LLAVEA cases_list default LLAVEC'
    t[0] = Switch(t[3], t[6], None, t[7], t.lineno(1), find_column(input, t.slice[1]))

def p_switch_2(t) :
    'switch_instr     : RSWITCH PARA expresion PARC LLAVEA cases_list LLAVEC'
    t[0] = Switch(t[3], None, t[6], None, t.lineno(1), find_column(input, t.slice[1]))

def p_switch_3(t) :
    'switch_instr     : RSWITCH PARA expresion PARC LLAVEA default LLAVEC'
    t[0] = Switch(t[3], None, None, t[6], t.lineno(1), find_column(input, t.slice[1]))

def p_cases_list_cases_list_case(t):
    'cases_list       : cases_list case'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
def p_cases_list_case(t):
    'cases_list       : case'
    if t[1] == "":
        t[0] = []
    else:
        t[0] = [t[1]]
        
def p_case(t):
    'case             : RCASE expresion DOSPUNTOS instrucciones'
    t[0] = Case(t[2], t[4], t.lineno(1), find_column(input, t.slice[1]))
    
def p_default(t):
    'default          : RDEFAULT DOSPUNTOS instrucciones'
    t[0] = t[3]
    
#///////////////////////////////////////WHILE//////////////////////////////////////////////////

def p_while(t) :
    'while_instr     : RWHILE PARA expresion PARC LLAVEA instrucciones LLAVEC'
    t[0] = While(t[3], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////FOR//////////////////////////////////////////////////

def p_for(t) :
    'for_instr     : RFOR PARA declaracion_asignacion PUNTOCOMA expresion PUNTOCOMA actualizacion PARC LLAVEA instrucciones LLAVEC'
    t[0] = For(t[3], t[5], t[7], t[10], t.lineno(1), find_column(input, t.slice[1]))
# def p_for(t) :
#     'for_instr     : RFOR PARA declaracion_instr PUNTOCOMA expresion PUNTOCOMA incremento_instr PARC LLAVEA instrucciones LLAVEC'
#     t[0] = For(t[3], t[5], t[7], t[10], t.lineno(1), find_column(input, t.slice[1]))
    
# #///////////////////////////////////////DEC_ASIG//////////////////////////////////////////////////

def p_declaracion_asignacion(t):
    '''declaracion_asignacion   :   declaracion_instr
                                |   asignacion_instr'''
    t[0] = t[1]
    
# #///////////////////////////////////////ACTUALIZACION//////////////////////////////////////////////////

def p_actualizacion(t):
    '''actualizacion    :   incremento_instr
                        |   decremento_instr
                        |   asignacion_instr
                        '''
    t[0] = t[1]
    
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

def p_funcion_1(t) :
    'funcion_instr     : RFUNC ID PARA parametros PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], t[4], t[7], t.lineno(1), find_column(input, t.slice[1]))

def p_funcion_2(t) :
    'funcion_instr     : RFUNC ID PARA PARC LLAVEA instrucciones LLAVEC'
    t[0] = Funcion(t[2], [], t[6], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////PARAMETROS//////////////////////////////////////////////////

def p_parametros_1(t):
    'parametros         : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_parametros_2(t):
    'parametros         : parametro'
    t[0] = [t[1]]
    
#///////////////////////////////////////PARAMETRO//////////////////////////////////////////////////
    
def p_parametro(t):
    'parametro          : tipo ID'
    t[0] = {'tipo':t[1], 'identificador':t[2]}

#///////////////////////////////////////LLAMADA A FUNCION//////////////////////////////////////////////////

def p_llamada_1(t) :
    'llamada_instr     : ID PARA PARC'
    t[0] = Llamada(t[1], [], t.lineno(1), find_column(input, t.slice[1]))
    
def p_llamada_2(t):
    'llamada_instr      : ID PARA parametros_llamada PARC'
    t[0] = Llamada(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////PARAMETROS LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametrosLL_1(t) :
    'parametros_llamada     : parametros_llamada COMA parametro_llamada'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_parametrosLL_2(t) :
    'parametros_llamada    : parametro_llamada'
    t[0] = [t[1]]

#///////////////////////////////////////PARAMETRO LLAMADA A FUNCION//////////////////////////////////////////////////

def p_parametroLL(t) :
    'parametro_llamada     : expresion'
    t[0] = t[1]


#///////////////////////////////////////TIPO//////////////////////////////////////////////////

def p_tipo(t) :
    '''tipo     : RINT
                | RFLOAT
                | RSTRING
                | RBOOLEAN
                 '''
    if t[1].lower() == 'int':
        t[0] = TIPO.ENTERO
    elif t[1].lower() == 'float':
        t[0] = TIPO.DECIMAL
    elif t[1].lower() == 'string':
        t[0] = TIPO.CADENA
    elif t[1].lower() == 'boolean':
        t[0] = TIPO.BOOLEANO

#///////////////////////////////////////EXPRESION//////////////////////////////////////////////////

def p_expresion_binaria(t):
    '''
    expresion           : expresion MAS expresion
                        | expresion MENOS expresion
                        | expresion POR expresion
                        | expresion DIV expresion
                        | expresion MOD expresion
                        | expresion POT expresion
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
    if t[2] == '*':
        t[0] = Aritmetica(OperadorAritmetico.POR, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '/':
        t[0] = Aritmetica(OperadorAritmetico.DIV, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '%':
        t[0] = Aritmetica(OperadorAritmetico.MOD, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
    if t[2] == '**':
        t[0] = Aritmetica(OperadorAritmetico.POT, t[1], t[3], t.lineno(2), find_column(input, t.slice[2]))
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
    
def p_expresion_char(t):
    '''expresion        : CHAR'''
    t[0] = Primitivos(TIPO.CHARACTER, str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))
    
def p_expresion_null(t):
    '''expresion        : RNULL'''
    t[0] = Primitivos(TIPO.NULO, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_true(t):
    '''expresion : RTRUE'''
    t[0] = Primitivos(TIPO.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_false(t):
    '''expresion : RFALSE'''
    t[0] = Primitivos(TIPO.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))

#///////////////////////////////////////ERROR//////////////////////////////////////////////////

def p_error(t):
    if t:
        parser.errok()
    else:
        print("Error sintactico en EOF")

def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Excepcion("Sintáctico","Error Sintáctico: " + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""

def p_instruccion_error1(t):
    'instruccion        : error'
    errores.append(Excepcion("Sintáctico","Error Sintáctico: " + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""

# def p_error(t):
#     if t != None:
#         errores.append(Excepcion("Sintáctico","Error Sintáctico." + str(t.value) , t.lineno, find_column(input, t)))
        # errores.append(Excepcion("Sintactico", "Error sintactico " + str(t[1].value) , t.lineno(1), find_column(input, t)))

#/////////////////////////////////////////////////////////////////////////////////////////

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
def analizar(entrada):
    # f = open("./entrada.txt", "r")
    # f = open("./archivo_02.jpr", "r")
    # entrada = f.read()

    from TS.Arbol import Arbol
    from TS.TablaSimbolos import TablaSimbolos

    instrucciones = parse(entrada.lower()) # ARBOL AST
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolos()
    ast.setTSglobal(TSGlobal)
    for error in errores:                   # CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
        ast.getExcepciones().append(error)
        ast.updateConsola(error.toString())

    if instrucciones == None:
        return ast
    
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
            if isinstance(value, Continue):
                err = Excepcion("Semantico", "Sentencia CONTINUE fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())
    contador = 0
    for instruccion in ast.getInstrucciones():      # 2DA PASADA (Main)
        
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
            if isinstance(value, Continue):
                err = Excepcion("Semantico", "Sentencia CONTINUE fuera de ciclo", instruccion.fila, instruccion.columna)
                ast.getExcepciones().append(err)
                ast.updateConsola(err.toString())

    for instruccion in ast.getInstrucciones():    # 3ERA PASADA (SENTENCIAS FUERA DE MAIN)
        if not (isinstance(instruccion, Main) or isinstance(instruccion, Declaracion) or isinstance(instruccion, Asignacion) or isinstance(instruccion, Funcion)):
            err = Excepcion("Semantico", "¡Sentencias fuera de función Main!", instruccion.fila, instruccion.columna)
            ast.getExcepciones().append(err)
            ast.updateConsola(err.toString())

    print(ast.getConsola())
    return ast