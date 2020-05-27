#Agenda de contactos | V1.0
#Programadores: Nicolás Rendón, Manuel Bermúdez, Oscar Julián
#Editor: Nicolás Rendón

# ============== Inicio del programa ==============

# Se importan las librerías

from tkinter import *
from tkinter import messagebox
from PIL import Image

# Se declaran las listas

lista = []   #Lista principal
lisImg = []  #lista imágenes
lisBlq = []  #lista bloqueos

# Se programan las funciones
# ======================================================

# Función borrar datos antiguos (modificar)

def modificar():
    modificado = conteliminar.get()
    cambiado = False
    for elemento in lista:
        arreglo = elemento.split('$')
        if conteliminar.get() == arreglo[1]:
            lista.remove(elemento)
            cambiado = True

    escribirContacto()
    consultar()

# Función actualizar datos nuevos (modificar)

def actualizar():
    n = nombre.get()
    ap = apellido.get()
    c = correo.get()
    t = telefono.get()
    f = foto.get()
    lista.append(n + '$' + ap + '$' + c + '$' + t + '$' + f)

    escribirContacto()
    messagebox.showinfo('Actualizar', 'El contacto se ha actualizado')

    nombre.set('')
    apellido.set('')
    telefono.set('')
    correo.set('')
    foto.set('')
    consultar()
    conFoto()

# Función refrescar página bloqueos (bloqueos)

def reload():
    r = Text(ventana, width=25, height=9)

    lisBlq.sort()
    valores = []
    r.insert(INSERT, 'Apodo\t\tBloqueado\n')

    for elemento in lisBlq:
        arreglo = elemento.split('$')
        valores.append(arreglo[0])
        r.insert(INSERT, arreglo[0] + '\t\n')

    r.place(x=490, y=430)
    etiquetaC = Label(ventana, text='Buscar: ', bg='#606060', fg=colorLetra).place(x=490, y=410)
    spinTelefono = Spinbox(ventana, value=(valores), textvariable=conteBloquear).place(x=550, y=410)
    if lista == []:
        etiquetaC = Label(ventana, text='Bloquear: ', bg='#606060', fg=colorLetra).place(x=470, y=380)
        spinTelefono = Spinbox(ventana, value=(valores)).place(x=500, y=400)
    r.configure(state=DISABLED)

# Función auxiliar para defBloquear (making lista bloqueos)

def bloq1():
    eliminado = conteliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split('$')
        if conteliminar.get() == arreglo[1]:
            lisBlq.append(arreglo[1])
            removido = True

    return lisBlq

# Función principal de bloqueos (bloqueos)

def bloquear():
    bloq1()
    r = Text(ventana, width=25, height=9)

    lisBlq.sort()
    valores = []
    r.insert(INSERT, 'Apodo\t\tBloqueado\n')

    for elemento in lisBlq:
        arreglo = elemento.split('$')
        valores.append(arreglo[0])
        r.insert(INSERT, arreglo[0] + '\t\n')

    r.place(x=490, y=430)
    etiquetaC = Label(ventana, text='Buscar: ', bg='#606060', fg=colorLetra).place(x=490, y=410)
    spinTelefono = Spinbox(ventana, value=(valores), textvariable=conteBloquear).place(x=550, y=410)
    if lista == []:
        etiquetaC = Label(ventana, text='Bloquear: ', bg='#606060', fg=colorLetra).place(x=470, y=380)
        spinTelefono = Spinbox(ventana, value=(valores)).place(x=500, y=400)
    r.configure(state=DISABLED)
    messagebox.showinfo('Bloquear', 'Contacto bloqueado')

# Función desbloqueo de contactos

def desbloquear():
    desbloqueado = conteBloquear.get()
    quitado = False
    for elemento in lisBlq:
        arreglo = elemento.split('$')
        if conteBloquear.get() == arreglo[0]:
            lisBlq.remove(elemento)
            quitado = True

    escribirContacto()
    reload()
    if quitado:
        messagebox.showinfo('Desbloquear', 'Contacto desbloqueado: ' + desbloqueado)

# Función-referencia mostrar imágenes con PIL

def mostrarImg():
    for x in lisImg:
        a = lisImg[x]

        # Leer Imagen

        im = Image.open(a)
        # Mostrar imagen
        im.show()


# Función guardar nuevo contacto

def guardar():
    n = nombre.get()
    ap = apellido.get()
    c = correo.get()
    t = telefono.get()
    f = foto.get()
    lista.append(n + '$' + ap + '$' + c + '$' + t + '$' + f)

    escribirContacto()
    messagebox.showinfo('Guardado', 'El contacto se ha guardado en tu agenda')

    nombre.set('')
    apellido.set('')
    telefono.set('')
    correo.set('')
    foto.set('')
    consultar()
    conFoto()

# Función eliminar contacto en spinbox

def eliminar():
    eliminado = conteliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split('$')
        if conteliminar.get() == arreglo[1]:
            lista.remove(elemento)
            removido = True

    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo('Eliminar', 'Contacto eliminado: ' + eliminado)


# Función contador de fotos
# Abre las fotos de contactos existentes en agenda y refresca la lista

def conFoto():
    lista.sort()
    valores = []

    for elemento in lista:
        arreglo = elemento.split('$')
        valores.append(arreglo[1])
        lisImg.append(arreglo[4])

        ###
        a = arreglo[4]

        # Leer Imagen

        im = Image.open(a)
        # Mostrar imagen
        im.show()
        ###


# Función consultar que imprime los contactos existentes y sus datos en formato tabla txt

def consultar():
    r = Text(ventana, width=80, height=15)

    lista.sort()
    valores = []
    r.insert(INSERT, 'Nombre\t\tApodo\t\tTeléfono\t\tCorreo\t\tFoto\n')

    for elemento in lista:
        arreglo = elemento.split('$')
        valores.append(arreglo[1])
        r.insert(INSERT, arreglo[0] + '\t\t' + arreglo[1] + '\t\t' + arreglo[3] + '\t\t' + arreglo[2] + '\t\t' + arreglo[4] + '\t\n')
        lisImg.append(arreglo[4])

    r.place(x=30, y=80)
    etiquetaC = Label(ventana, text='Buscar: ', bg='#606060', fg=colorLetra).place(x=230, y=380)
    spinTelefono = Spinbox(ventana, value=(valores), textvariable=conteliminar).place(x=280, y=380)
    if lista == []:
        etiquetaC = Label(ventana, text='Buscar: ', bg='#606060', fg=colorLetra).place(x=230, y=380)
        spinTelefono = Spinbox(ventana, value=(valores)).place(x=280, y=380)
    r.configure(state=DISABLED)

# Función iniciar el archivo con datos guardados en disco duro

def iniciarArchivo():
    archivo = open('ag.txt', 'a')
    archivo.close()


# Función que carga el archivo con datos existentes

def cargar():
    archivo = open('ag.txt', 'r')
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

# Función que escribe los datos de los contactos en el archivo de texto sin formato

def escribirContacto():
    archivo = open('ag.txt', 'w')
    lista.sort()
    lisBlq.sort()

    for elemento in lista:
        archivo.write(elemento + '\n')

    for elemento in lisBlq:
        archivo.write(elemento + '\n')

    archivo.close()

# Función que muestra datos del programa y desarrolladores al usuario
# Es llamada por el botón 'Acerca de'

def ventanaDos():
    # Leer Imagen
    im = Image.open('info.png')
    # Mostrar imagen
    im.show()

# Función que muestra el diagrama de clases UML
# Es llamada por el botón 'Diagrama'

def ventanaTres():
    # Leer Imagen
    im = Image.open('diag.png')
    # Mostrar imagen
    im.show()

# ============================ Inicio creación interfaz de usuario con TK ============================
# Parametrizar la ventana

ventana = Tk()

nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
correo = StringVar()
foto = StringVar()
conteliminar = StringVar()
conteModificar = StringVar()
conteBloquear = StringVar()
colorLetra = '#FFF'

# Llamado a las funciones

iniciarArchivo()
cargar()
consultar()


ventana.title('Agenda de contactos')
ventana.geometry('700x600')
Fondo= PhotoImage(file='prueba-1.png')
colorFondo = Label(ventana,image=Fondo).place(x=0,y=0)
#colorFondo = '#000'
ventana.configure(background=colorFondo)

# Creación de etiquetas, botones, captura de los StringVar, Spinboxes...

# ======================= Zona de etiquetas =======================

etiquetaTitulo = Label(ventana, text='Agenda de contactos', bg='#404040', fg=colorLetra, font=('Helvetica', 20)).place(
    x=220, y=15)

etiquetaN = Label(ventana, text='Nombre: ', bg='#404040', fg=colorLetra).place(x=20, y=400)
cajaN = Entry(ventana, textvariable=nombre).place(x=80, y=400)

etiquetaAp = Label(ventana, text='Apodo: ', bg='#404040', fg=colorLetra).place(x=20, y=430)
cajaAp = Entry(ventana, textvariable=apellido).place(x=80, y=430)

etiquetaT = Label(ventana, text='Teléfono: ', bg='#404040', fg=colorLetra).place(x=20, y=460)
cajaT = Entry(ventana, textvariable=telefono).place(x=80, y=460)

etiquetaC = Label(ventana, text='Correo: ', bg='#404040', fg=colorLetra).place(x=20, y=490)
cajaC = Entry(ventana, textvariable=correo).place(x=80, y=490)

etiquetaF = Label(ventana, text='Foto: ', bg='#404040', fg=colorLetra).place(x=20, y=520)
cajaF = Entry(ventana, textvariable=foto).place(x=80, y=520)


# ======================= Zona de botones =======================

botonGuardar = Button(ventana, text='Guardar', command=guardar, bg='green', fg='white').place(x=80, y=550)

botonBloquear = Button(ventana, text='Bloquear', command=bloquear, bg='#404040', fg='white').place(x=490, y=380)
botonEliminar = Button(ventana, text='Eliminar', command=eliminar, bg='red', fg='white').place(x=420, y=380)
botonDesbloquear = Button(ventana, text='Desbloquear', command=desbloquear, bg='#009', fg='white').place(x=550,
                                                                                                            y=380)

botonInfo = Button(ventana, text='Acerca de', command=ventanaDos, bg='blue', fg='white').place(x=80, y=20)
botonDiag = Button(ventana, text='Diagrama', command=ventanaTres, bg='blue', fg='white').place(x=590, y=20)

botonModificar = Button(ventana, text='Modificar', command=modificar, bg='yellow', fg='black').place(x=330, y=575)
botonActual = Button(ventana, text='Actualizar', command=actualizar, bg='yellow', fg='black').place(x=392, y=575)

# ======================= Zona etiquetas para contactos modificados =======================

etiquetaN2 = Label(ventana, text='Nuevo nombre: ', bg='#404040', fg=colorLetra).place(x=230, y=430)
cajaN2 = Entry(ventana, textvariable=nombre).place(x=330, y=430)

etiquetaAp2 = Label(ventana, text='Nuevo apodo: ', bg='#404040', fg=colorLetra).place(x=230, y=460)
cajaAp2 = Entry(ventana, textvariable=apellido).place(x=330, y=460)

etiquetaT2 = Label(ventana, text='Nuevo teléfono: ', bg='#404040', fg=colorLetra).place(x=230, y=490)
cajaT2 = Entry(ventana, textvariable=telefono).place(x=330, y=490)

etiquetaC2 = Label(ventana, text='Nuevo correo: ', bg='#404040', fg=colorLetra).place(x=230, y=520)
cajaC2 = Entry(ventana, textvariable=correo).place(x=330, y=520)

etiquetaF2 = Label(ventana, text='Nueva foto: ', bg='#404040', fg=colorLetra).place(x=230, y=550)
cajaF2 = Entry(ventana, textvariable=foto).place(x=330, y=550)

# Llamado a la ejecución del loop principal en la ventana de TK...
mainloop()

# ======================= Fin del programa =======================