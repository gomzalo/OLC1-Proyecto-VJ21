from tkinter import *
import os
import re
import tkinter as tk 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
import tkinter.font as font
from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos
from grammar import analizar, debug_btn, getErrores, parse, errores, debugger
from TS.Excepcion import Excepcion
window = Tk()

archivo = ""
varibale = "test"
cont = -1
contador = 0

def salir(): 
    #print("Entre a salir"); 
    value = messagebox.askokcancel("Salir", "¿Está seguro que desea salir?")
    if value :
        window.destroy()
        
def guardar_archivo(): 
    global archivo
    if archivo == "":
        guardar_como()
    else:
        guardarc = open(archivo, "w", encoding="utf8")
        guardarc.write(ta_editor.get(1.0, END))
        guardarc.close()

#Guardar Como
def guardar_como():      
    global archivo
    guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "D:\G\Documents\GitHub\OLC1-Proyecto-VJ21\Entrada")
    fguardar = open(guardar, "w+", encoding="utf8")
    fguardar.write(ta_editor.get(1.0, END))
    fguardar.close()
    archivo = guardar

#Crear nuevo_archivo
def nuevo_archivo():   
    global archivo
    ta_editor.delete(1.0, END)
    archivo = ""

def get_consola():
    ta_consola.config(state=NORMAL)
    ta_consola.insert(1.0, varibale)
    ta_consola.mark_set(INSERT,END)
    ta_consola.see(INSERT)
    ta_consola.config(state=DISABLED)


#Abrir archivo
def abrir():
    global archivo
    archivo = filedialog.askopenfilename(title = "Abrir Archivo", initialdir = "D:\G\Documents\GitHub\OLC1-Proyecto-VJ21\Entrada")

    contenido_archivo = open(archivo, encoding="utf8")
    content = contenido_archivo.read()

    ta_editor.delete(1.0, END)
    for s in recorrerInput(content):
        ta_editor.insert(INSERT, s[1], s[0])
    contenido_archivo.close()

def paint():
    pos_cur = ta_editor.index(INSERT)
    texto_obtenido = ta_editor.get(1.0, END)
    ta_editor.delete(1.0, END)

    for s in recorrerInput(texto_obtenido):
        ta_editor.insert(INSERT, s[1], s[0])
    ta_editor.mark_set("insert", pos_cur)
    ta_editor.see("insert")


def update_line(*args):      
    lines.delete("all")
    cont = ta_editor.index("@1,0")
    
    while True :
        dline= ta_editor.dlineinfo(cont)
        if dline is None: 
            break
        y = dline[1]
        strline = str(cont).split(".")[0]
        lines.create_text(2,y,anchor="nw", text=strline, fill="#6d70a9", font = ("Arial", 8))
        cont = ta_editor.index("%s+1line" % cont)

def posicion(event):
    pos.config(text = "Linea " + str(ta_editor.index(INSERT)).replace(".","   Columna ") + "" )
    update_line()
    paint()


# Pintar palabras
def recorrerInput(i):  #Funcion para get_consola palabrvas reservadas, signos, numeros, etc
    lista = []
    val = ''
    counter = 0
    while counter < len(i):
        if re.search(r"[A-Za-z]", i[counter]):
            val += i[counter]
        elif i[counter] == "$":
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            val = "$"
        elif i[counter] == "1" or i[counter] == "2" or i[counter] == "3" or i[counter] == "4" or i[counter] == "5" or i[counter] == "6" or i[counter] == "7" or i[counter] == "8" or i[counter] == "9" or i[counter] == "10" or i[counter] == "11" or i[counter] == "12" or i[counter] == "13" or i[counter] == "14" or i[counter] == "15" or i[counter] == "16" or i[counter] == "17" or i[counter] == "18" or i[counter] == "19" or i[counter] == "20" or i[counter] == "21" or i[counter] == "22" or i[counter] == "23" or i[counter] == "24" or i[counter] == "25" or i[counter] == "26" or i[counter] == "27" or i[counter] == "28" or i[counter] == "29" or i[counter] == "30" or i[counter] == "31" or i[counter] == "32" or i[counter] == "33" or i[counter] == "34" or i[counter] == "35" or i[counter] == "36" or i[counter] == "37" or i[counter] == "38" or i[counter] == "39" or i[counter] == "40" or i[counter] == "0":
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            l = []
            l.append("numeros")
            l.append(i[counter])
            lista.append(l)
        elif i[counter] == "\"":
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            val = i[counter]
            counter += 1
            while counter < len(i):
                if i[counter] == "\"":
                    val += i[counter]
                    l = []
                    l.append("cadena")
                    l.append(val)
                    lista.append(l)
                    val = ''
                    break
                val += i[counter]
                counter += 1
                if(counter==len(i)):
                    l = []
                    l.append("normal")
                    l.append(val[0:-1])
                    lista.append(l)
                    val = ''

        elif i[counter] == "#":
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
                #print(val)
            val = i[counter]
            counter += 1
            if i[counter] =="*":
                val += i[counter]
                counter += 1
                while counter < len(i):
                    if i[counter] == "*":
                        if i[counter+1] == "#":
                            val += i[counter]
                            l = []
                            l.append("comentariomulti")
                            l.append(val)
                            lista.append(l)
                            val = ''
                            break
                    val += i[counter]
                    counter += 1
                    if(counter==len(i)):
                        l = []
                        l.append("normal")
                        l.append(val[0:-1])
                        lista.append(l)
                        val = ''
            else:
                while counter < len(i):
                    if i[counter] == "\n" or counter+1== len(i):
                        val += i[counter]
                        l = []
                        l.append("comentario")
                        l.append(val)
                        lista.append(l)
                        val = ''
                        break
                    val += i[counter]
                    counter += 1

        elif i[counter] == "\'":
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            val = i[counter]
            counter += 1
            while counter < len(i):
                if i[counter] == "\'":
                    val += i[counter]
                    l = []
                    l.append("caracteres")
                    l.append(val)
                    lista.append(l)
                    val = ''
                    break
                val += i[counter]
                counter += 1
                if(counter==len(i)):
                    l = []
                    l.append("normal")
                    l.append(val[0:-1])
                    lista.append(l)
                    val = ''
        else:
            if len(val) != 0:
                l = []
                l.append("variable")
                l.append(val)
                lista.append(l)
                val = ''
            l = []
            l.append("signo")
            l.append(i[counter])
            lista.append(l)

        counter +=1

    for s in lista:
        if s[1] == 'int' or s[1] == 'double' or s[1] == 'boolean' or s[1] == 'char' or s[1] == 'string' or s[1] == 'null' or s[1] == 'var' or s[1] == 'new' or s[1] == 'if' or s[1] == 'else' or s[1] == 'print' or s[1] == 'switch' or s[1] == 'case' or s[1] == 'default' or s[1] == 'continue' or s[1] == 'while' or s[1] == 'for' or s[1] == 'return' or s[1] == 'func' or s[1] == 'read' or s[1] == 'toLower' or s[1] == 'toUpper' or s[1] == 'length' or s[1] == 'truncate' or s[1] == 'round' or s[1] == 'typeof' or s[1] == 'main' or s[1] == 'break' or s[1] == 'float' or s[1] == 'true' or s[1] == 'false' :
            s[0] = 'reservada'
        elif s[1][0] != "$":
            if s[0] == 'variable':
                s[0] = 'etiqueta'
    
    if len(lista)>0: #Si tamano de la listaes mayor a 0 -->si viene algo
        if lista[len(lista)-1][1]=='\n': #a la lista en la ultima posicion su valor es un salto de linea
            lista.pop(len(lista)-1)
    return lista

ast = None

#Compilar
def compilar():
    global ast
    ta_consola.config(state=NORMAL)
    ta_consola.delete(1.0, END)
    texto_obtenido = ta_editor.get("1.0", END)
    ast = analizar(texto_obtenido)
    ta_consola.insert(END, ast.getConsola())
    ta_consola.config(state=DISABLED)
#Errores
def errores():
    if ast != None:
        ta_reporte_errores.config(state=NORMAL)
        ta_reporte_errores.delete(1.0, END)
        for error in ast.getExcepciones():
            ta_reporte_errores.insert(END, error.toString())
            ta_reporte_errores.insert(END, "\n")
        ta_reporte_errores.config(state=DISABLED) 
#Graficar AST
def graficar_ast():
    os.system('dot -T pdf -o ast.pdf ast.dot')
    dirname = os.path.dirname(__file__)
    direc = os.path.join(dirname, 'ast.pdf')
    os.system(direc)
#Debugger

def debug():
    # global ast
    global contador
    # print("contador window: " + str(contador))
    ta_consola.config(state=NORMAL)
    ta_consola.delete(1.0, END)
    texto_obtenido = ta_editor.get("1.0", END)
    debugger(texto_obtenido)
    content = debug_btn(texto_obtenido)
    # contador += 1
    ta_consola.insert(END, content)
    ta_consola.config(state=DISABLED)
    

# Window properties
window.title("JPR")
window.geometry("1400x720+0+0")
window.config(bg="#282a36")


# Text area
ta_editor = scrolledtext.ScrolledText(window, width=75, height=15, wrap=tk.WORD, font=('Arial', 12), background = '#292640')
ta_editor.place(x=25, y=130)
ta_editor.focus()

ta_consola = scrolledtext.ScrolledText(window, width=60, height=15, wrap=tk.WORD, font=('Arial', 12), background = '#001629', fg = "#7A90CA")
ta_consola.place(x=755, y=130)
ta_consola.focus()
ta_consola.config(state=DISABLED)

ta_reporte_errores = scrolledtext.ScrolledText(window, width=115, height=10, wrap=tk.WORD, font=('Courier New', 12), background = '#0a0f0b', fg = "#49e9a6")
ta_reporte_errores.place(x=55, y=470)
ta_reporte_errores.focus()
ta_reporte_errores.config(state=DISABLED)

# COLORES
ta_editor.tag_config('reservada', foreground='#16a3b3')
ta_editor.tag_config('cadena', foreground='#d98661')
ta_editor.tag_config('caracteres', foreground='#d98661')
ta_editor.tag_config('comentariomulti', foreground='#716c93')
ta_editor.tag_config('comentario', foreground='#716c93')
ta_editor.tag_config('numeros', foreground='#65428d')

ta_editor.tag_config('variable', foreground='#e4b781')
ta_editor.tag_config('operacion', foreground='#e4b781')
ta_editor.tag_config('etiqueta', foreground='#e4b781')

#Funcionalidad del teclado
ta_editor.bind('<Return>', update_line)
ta_editor.bind('<BackSpace>', update_line)
ta_editor.bind('<<Change>>', update_line)
ta_editor.bind('<Configure>', update_line)
ta_editor.bind('<Motion>', update_line)
ta_editor.bind('<Button-1>', posicion)
ta_editor.bind('<KeyRelease>', posicion)

#Contador de lineas
lines = Canvas(window, width = 25, height = 275, background = '#1f1d30', highlightthickness=0)
lines.place(x=2, y=130)

pos = ttk.Label(window, text = cont, background='#1f1d30')
pos.place(x=30, y=410)

fuente_30 = font.Font(size=30)
fuente_10 = font.Font(size=16)
# Compilar button
boton_compilar = Button(window, width=15, height=2, text="Compilar", background = '#30243d', fg='#716c93', command=compilar)
boton_compilar.place(x=350, y=655)
boton_compilar['font'] = fuente_10
# Siguiente button
boton_seguir = Button(window, width=15, height=2, text="Siguiente", background = '#30243d', fg='#716c93', command =  debug)
boton_seguir.place(x=910, y=655)
boton_seguir['font'] = fuente_10
# Labels
lb_editor = Label(window, width=15, height=2, text="Editor", bg='#0d1117', fg='#58a6ff')
lb_editor.place(x=215, y=20)
lb_editor['font'] = fuente_30
lb_consola = Label(window, width=15, height=2, text="Consola", bg='#0d1117', fg='#58a6ff')
lb_consola.place(x=865, y=20)
lb_consola['font'] = fuente_30
lb_errores = Label(window, width=15, height=2, text="Reporte de errores", bg='#0d1117', fg='#58a6ff')
lb_errores.place(x=650, y=410)
lb_errores['font'] = fuente_10

# Bar menu
menubar = Menu(window)
window.config(menu=menubar, background='#282a36' )

fileMenu = Menu(menubar, tearoff=0, background = '#30363d')
fileMenu1 = Menu(menubar, tearoff=0, background = '#30363d')
fileMenu2 = Menu(menubar, tearoff=0, background = '#30363d')
fileMenu3 = Menu(menubar, tearoff=0, background = '#30363d')

menubar.add_cascade(label = "Archivo", menu = fileMenu)
fileMenu.add_command(label ="Crear archivos", command = nuevo_archivo, foreground='#bcb1c7', activeforeground='#5f5ba8')
fileMenu.add_command(label ="Abrir archivo", command = abrir,foreground='#bcb1c7',  activeforeground='#5f5ba8')
fileMenu.add_command(label ="Guardar", command = guardar_archivo, foreground='#bcb1c7', activeforeground='#5f5ba8')
fileMenu.add_command(label ="Guardar Como", command = guardar_como, foreground='#bcb1c7', activeforeground='#5f5ba8')
fileMenu.add_separator()

menubar.add_cascade(label = "Herramientas", menu = fileMenu1)
fileMenu1.add_command(label ="Interpretar", command = compilar, foreground='#bcb1c7', activeforeground='#5f5ba8')
fileMenu1.add_command(label ="Debugger", command =  debug, foreground='#bcb1c7', activeforeground='#5f5ba8')

menubar.add_cascade(label = "Reportes", menu = fileMenu2, activeforeground='#5f5ba8')
fileMenu2.add_command(label ="Reporte de Errores", command=errores, foreground='#bcb1c7', activeforeground='#5f5ba8')
fileMenu2.add_command(label ="Generar Arbol AST", command=graficar_ast, foreground='#bcb1c7', activeforeground='#5f5ba8')
fileMenu2.add_command(label ="Reporte de Tabla de Simbolos", foreground='#bcb1c7', activeforeground='#5f5ba8')

window.mainloop()