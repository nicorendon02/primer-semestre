from tkinter import *
from tkinter import messagebox

lista = []

def modificar():
    pass

def bloquear():
    pass

def guardar():
    n = nombre.get()
    ap = apellido.get()
    c = correo.get()
    t = telefono.get()
    lista.append(n+'$'+ap+'$'+c+'$'+t)
    escribirContacto()
    messagebox.showinfo('Guardado','El contacto ha sido guardado exitosamente')

    nombre.set('')
    apellido.set('')
    telefono.set('')
    correo.set('')
    consultar()

def eliminar():
    eliminado = conteliminar.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split('$')
        if conteliminar.get() == arreglo[2]:
            lista.remove(elemento)
            removido = True

    escribirContacto()
    consultar()
    if removido:
        messagebox.showinfo('Eliminar','Elemento eliminado: '+eliminado)


def consultar():
    r = Text(ventana,width=80,height=15)
    lista.sort()
    valores = []
    r.insert(INSERT,'Nombre\t\tApellido\t\tTelefono\t\tCorreo\n')
    for elemento in lista:
        arreglo = elemento.split('$')
        valores.append(arreglo[2])
        r.insert(INSERT,arreglo[0]+'\t\t'+arreglo[1]+'\t\t'+arreglo[3]+'\t\t'+arreglo[2]+'\t\n')
    r.place(x=20,y=230)
    spinTelefono = Spinbox(ventana,value=(valores),textvariable=conteliminar).place(x=450,y=50)
    if lista ==[]:
        spinTelefono = Spinbox(ventana,value=(valores)).place(x=450,y=50)
    r.configure(state=DISABLED)

def iniciarArchivo():
    archivo = open('ag.txt','a')
    archivo.close()

def cargar():
    archivo = open('ag.txt','r')
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()

def escribirContacto():
    archivo = open('ag.txt','w')
    lista.sort()
    for elemento in lista:
        archivo.write(elemento+'\n')
    archivo.close()


ventana = Tk()

nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
correo = StringVar()
conteliminar = StringVar()
colorLetra = '#FFF'

iniciarArchivo()
cargar()
consultar()

ventana.title('Agenda de contactos')
ventana.geometry('700x500')
Fondo= PhotoImage(file='prueba-1.png')
colorFondo = Label(ventana,image=Fondo).place(x=0,y=0)
#ventana.configure(background=colorFondo)

etiquetaTitulo = Label(ventana, text='Agenda de contactos', bg='#404040', fg=colorLetra,font=('Helvetica', 18)).place(x=220,y=8)
etiquetaN = Label(ventana,text='Nombre: ',bg='#404040',fg=colorLetra).place(x=50,y=80)
cajaN = Entry(ventana,textvariable=nombre).place(x=150,y=80)

etiquetaAp = Label(ventana,text='Apellido: ',bg='#404040',fg=colorLetra).place(x=50,y=110)
cajaAp = Entry(ventana,textvariable=apellido).place(x=150,y=110)

etiquetaT = Label(ventana,text='Telefono: ',bg='#404040',fg=colorLetra).place(x=50,y=140)
cajaT = Entry(ventana,textvariable=telefono).place(x=150,y=140)

etiquetaC = Label(ventana,text='Correo: ',bg='#404040',fg=colorLetra).place(x=50,y=170)
cajaC = Entry(ventana,textvariable=correo).place(x=150,y=170)

etiquetaEliminar = Label(ventana,text='Buscar correo: ', bg='#404040',fg=colorLetra).place(x=340,y=80)
spinTelefono = Spinbox(ventana,textvariable=conteliminar).place(x=430,y=80)

botonGuardar = Button(ventana,text='Guardar',command=guardar,bg='#009',fg='white').place(x=180,y=200)
botonModificar = Button(ventana,text='Modificar',command=eliminar,bg='#009',fg='white').place(x=470,y=110)
botonBloquear = Button(ventana,text='Bloquear',command=eliminar,bg='#009',fg='white').place(x=470,y=140)
botonEliminar = Button(ventana,text='Eliminar',command=eliminar,bg='#009',fg='white').place(x=470,y=170)

enunciadoAmigos = Label(ventana,text='Tus amigos, en un solo lugar',bg='#404040',fg=colorLetra,font=('Helvetica', 16)).place(x=200,y=420)

mainloop()
