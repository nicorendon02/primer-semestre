from tkinter import *
from tkinter import messagebox
from PIL import Image

lista = []
lisImg = []

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


def actualizar():
    n = nombre.get()
    ap = apellido.get()
    c = correo.get()
    t = telefono.get()
    lista.append(n + '$' + ap + '$' + c + '$' + t)
    escribirContacto()
    messagebox.showinfo('Actualizado', 'Tu agenda está actualizada')

    nombre.set('')
    apellido.set('')
    telefono.set('')
    correo.set('')
    consultar()


def bloquear():
    pass


def desbloquear():
    pass


def mostrarImg():
    for x in lisImg:
        a = lisImg[x]

        # Leer Imagen

        im = Image.open(a)
        # Mostrar imagen
        im.show()


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

        ###
        a = arreglo[4]

        # Leer Imagen

        im = Image.open(a)
        # Mostrar imagen
        im.show()
        ###

    r.place(x=30, y=80)
    etiquetaC = Label(ventana, text='Buscar: ', bg='#606060', fg=colorLetra).place(x=230, y=380)
    spinTelefono = Spinbox(ventana, value=(valores), textvariable=conteliminar).place(x=280, y=380)
    if lista == []:
        etiquetaC = Label(ventana, text='Buscar: ', bg='#606060', fg=colorLetra).place(x=230, y=380)
        spinTelefono = Spinbox(ventana, value=(valores)).place(x=280, y=380)
    r.configure(state=DISABLED)


def iniciarArchivo():
    archivo = open('ag.txt', 'a')
    archivo.close()


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


def escribirContacto():
    archivo = open('ag.txt', 'w')
    lista.sort()
    for elemento in lista:
        archivo.write(elemento + '\n')
    archivo.close()


def ventanaDos():
    ventana2 = Tk()
    ventana2.title('Acerca de')
    ventana2.geometry('700x524')
    ventana2.state("normal")
    ventana2.deiconify()


ventana = Tk()

nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
correo = StringVar()
foto = StringVar()
conteliminar = StringVar()
conteModificar = StringVar()
colorLetra = '#FFF'

iniciarArchivo()
cargar()
consultar()


ventana.title('Agenda de contactos')
ventana.geometry('700x580')
# Fondo= PhotoImage(file='prueba-1.png')
# colorFondo = Label(ventana,image=Fondo).place(x=0,y=0)
colorFondo = '#000'
# ventana.configure(background=colorFondo)

etiquetaTitulo = Label(ventana, text='Agenda de contactos', bg='#404040', fg=colorLetra, font=('Helvetica', 20)).place(
    x=220, y=20)

etiquetaN = Label(ventana, text='Nombre: ', bg='#606060', fg=colorLetra).place(x=10, y=380)
cajaN = Entry(ventana, textvariable=nombre).place(x=70, y=380)

etiquetaAp = Label(ventana, text='Apodo: ', bg='#606060', fg=colorLetra).place(x=10, y=410)
cajaAp = Entry(ventana, textvariable=apellido).place(x=70, y=410)

etiquetaT = Label(ventana, text='Teléfono: ', bg='#606060', fg=colorLetra).place(x=10, y=440)
cajaT = Entry(ventana, textvariable=telefono).place(x=70, y=440)

etiquetaC = Label(ventana, text='Correo: ', bg='#606060', fg=colorLetra).place(x=10, y=470)
cajaC = Entry(ventana, textvariable=correo).place(x=70, y=470)

etiquetaF = Label(ventana, text='Foto: ', bg='#606060', fg=colorLetra).place(x=10, y=500)
cajaF = Entry(ventana, textvariable=foto).place(x=70, y=500)

# etiquetaEliminar5 = Label(ventana,text='Desbloquear contacto: ', bg='#404040',fg=colorLetra).place(x=315,y=230)
# spinTelefono5 = Spinbox(ventana,textvariable=conteliminar).place(x=440,y=230)


botonGuardar = Button(ventana, text='Guardar', command=guardar, bg='green', fg='white').place(x=70, y=530)

botonBloquear = Button(ventana, text='Bloquear', command=bloquear, bg='#009', fg='white').place(x=590, y=400)
botonEliminar = Button(ventana, text='Eliminar', command=eliminar, bg='red', fg='white').place(x=420, y=380)
botonDesbloquear = Button(ventana, text='Desbloquear', command=desbloquear, bg='#404040', fg='white').place(x=590,
                                                                                                            y=380)

botonInfo = Button(ventana, text='Acerca de', command=ventanaDos, bg='blue', fg='white').place(x=70, y=10)

botonModificar = Button(ventana, text='Modificar', command=modificar, bg='yellow', fg='black').place(x=360, y=550)
botonActual = Button(ventana, text='Actualizar', command=actualizar, bg='yellow', fg='black').place(x=330, y=550)

etiquetaN2 = Label(ventana, text='Nuevo nombre: ', bg='#606060', fg=colorLetra).place(x=230, y=410)
cajaN2 = Entry(ventana, textvariable=nombre).place(x=330, y=410)

etiquetaAp2 = Label(ventana, text='Nuevo apodo: ', bg='#606060', fg=colorLetra).place(x=230, y=440)
cajaAp2 = Entry(ventana, textvariable=apellido).place(x=330, y=440)

etiquetaT2 = Label(ventana, text='Nuevo teléfono: ', bg='#606060', fg=colorLetra).place(x=230, y=470)
cajaT2 = Entry(ventana, textvariable=telefono).place(x=330, y=470)

etiquetaC2 = Label(ventana, text='Nuevo correo: ', bg='#606060', fg=colorLetra).place(x=230, y=500)
cajaC2 = Entry(ventana, textvariable=correo).place(x=330, y=500)

etiquetaF2 = Label(ventana, text='Nueva foto: ', bg='#606060', fg=colorLetra).place(x=230, y=530)
cajaF2 = Entry(ventana, textvariable=foto).place(x=330, y=530)



mainloop()