# Vamos a hacer una interfaz para que se vea lindo, importemos tkinter
import tkinter as TK
from tkinter import messagebox as msg

# Importamos el socket, que es para la cosa del servidor y cliente.
import socket

# Importamos pickle para mandar una lista en lugar de un solo string
import pickle

# Importamos las validaciones.
import validacionesYCalculos as ValCal

# Importamos las funciones para leer los txt
import leerTxt as leer

# Configuramos la conexión con el servidor.
port = 666  # Escojemos el puerto.
server = socket.gethostbyname(socket.gethostname())  # Dirección IPv4
address = (server, port)  # Dirección
format = "utf-8"  # formato en el que vamos a codificar y decodificar.

# Creamos un socket para el cliente y lo conectamos al server.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)

# Boton para ver si podemos leer el txt de entrada
puedeLeerTexto = False


def leerMensajeEntrada():
    if puedeLeerTexto:
        mensaje = leer.leerTexto("mensajedeentrada.txt")
        print(mensaje)
    else:
        msg.showerror(
            title="ERROR", message="Aun no se validan las contraseñas cliente/servidor")


def insertarLog(listaLogs):
    # Vamos insertando uno a uno los logs.
    # Se borra lo que pueda estar escrito en la casilla de las interacciones
    interacciónClienteServidor.delete("1.0", "end")

    for log in listaLogs:
        # Se escribe en la casilla de mensaje el resultado
        interacciónClienteServidor.insert("end", log + "\n")


def enviarDatos(AoK, p, g, BoK):
    listaDatos = [AoK, p, g, BoK]
    data = pickle.dumps(listaDatos)
    client.send(data)

# Función para enviar variables desde el cliente al servidor.


def enviarVariables():

    # Primero se valida que las variables sean valores numéricos.
    if ValCal.letrasChiquitasNumericas(aChiquita.get(), gChiquita.get(), pChiquita.get()):

        # Se transforman de string a int
        achiquitaNumero = int(aChiquita.get())
        gchiquitaNumero = int(gChiquita.get())
        pchiquitaNumero = int(pChiquita.get())

        # Validamos que sean números enteros y las validaciónes generales que son
        # P debe ser un número primo
        # a debe ser un número entre 0 y P-1
        # g debe ser un número entre 0 y P
        if(ValCal.letrasChiquitasEnteras(achiquitaNumero, gchiquitaNumero, pchiquitaNumero) and
           ValCal.validacionesVariablesCliente(achiquitaNumero, pchiquitaNumero, gchiquitaNumero)):

            # Listado de los logs
            listaLogs = []

            # Calculamos la A del cliente.
            Acliente = ValCal.calcularAoB(
                gchiquitaNumero, achiquitaNumero, pchiquitaNumero)
            # Añadimos a la lista de logs
            listaLogs.append(
                "El cliente le envió al servidor, A = " + str(Acliente))

            # Enviamos el A para que el servidor calcule el B
            enviarDatos(Acliente, pchiquitaNumero, gchiquitaNumero, "B")

            # Recogemos el B del servidor.
            BServidor = int(client.recv(1024).decode())
            # Añadimos a la lista de logs
            listaLogs.append(
                "El servidor le envió al cliente, B = " + str(BServidor))

            # Calculamos K del cliente
            Kcliente = ValCal.calcularK(
                BServidor, achiquitaNumero, pchiquitaNumero)
            # Añadimos a la lista de logs
            listaLogs.append(
                "El cliente le envió al servidor, K = " + str(Kcliente))

            # Enviamos los mismos datos, pero ahora queremos calcular la K del servidor.
            enviarDatos(Acliente, pchiquitaNumero, gchiquitaNumero, "K")

            # Recogemos la K del servidor.
            Kserver = int(client.recv(1024).decode())
            # Añadimos a la lista de logs
            listaLogs.append(
                "El servidor le envió al cliente, K = " + str(Kserver))

            insertarLog(listaLogs)

            # Verificamos que sean iguales
            if Kcliente == Kserver:

                global puedeLeerTexto
                puedeLeerTexto = True


# Creamos la ventana
ventana = TK.Tk()
ventana.geometry("1000x500")
ventana.resizable(height=False, width=False)
ventana.title("Menú del cliente")
ventana.iconbitmap("miko.ico")

# Fondito
pantalla = TK.PhotoImage(file="akukin.png")
fotopantalla = TK.Label(ventana, image=pantalla)
fotopantalla.place(x=0, y=0)

# Lado derecho de Aqua
# Este es el cosito que dice interacción cliente/servidor
interacciónClienteServidorLabel = TK.Label(
    ventana, text="Interacción cliente/servidor")
interacciónClienteServidorLabel.place(x=650, y=50, width=330)

# Acá se pondrá el log entre el cliente y el servidor.
interacciónClienteServidor = TK.Text(ventana)
interacciónClienteServidor.place(x=650, y=70, width=330, height=125)

# Este es el cosito que dice mensaje txt
mensajeEntradaLabel = TK.Label(
    ventana, text="Mensaje")
mensajeEntradaLabel.place(x=650, y=225, width=330)

# Acá se pondrá el log entre el cliente y el servidor.
mensajeEntrada = TK.Text(ventana)
mensajeEntrada.place(x=650, y=245, width=330, height=125)

# Lado izquierdo de Aqua
# Este es el cosito que dice menú del cliente
menuClienteLabel = TK.Label(ventana, text="Menú del cliente")
menuClienteLabel.place(x=100, y=50, width=190)

# Título para la a pequeña
aChiquitaLabel = TK.Label(ventana, text="Introduzca 'a'")
aChiquitaLabel.place(x=100, y=80, width=190)

# Acá se pondrá la a chiquitita del cliente.
aChiquita = TK.Entry(ventana)
aChiquita.place(x=100, y=100, width=190, height=20)

# Título para la g pequeña
gChiquitaLabel = TK.Label(ventana, text="Introduzca 'g'")
gChiquitaLabel.place(x=100, y=130, width=190)

# Acá se pondrá la g del cliente.
gChiquita = TK.Entry(ventana)
gChiquita.place(x=100, y=150, width=190, height=20)

# Título para la p pequeña
pChiquitaLabel = TK.Label(ventana, text="Introduzca 'P'")
pChiquitaLabel.place(x=100, y=180, width=190)

# Acá se pondrá la p del cliente.
pChiquita = TK.Entry(ventana)
pChiquita.place(x=100, y=200, width=190, height=20)

# Boton para mandar los datos
TK.Button(
    ventana,
    text="Enviar variables",
    command=lambda: enviarVariables()
).place(x=100, y=230, width=190)

# Boton para mandar leer el archivo txt de entrada
TK.Button(
    ventana,
    text="Leer txt de entrada",
    command=lambda: leerMensajeEntrada()
).place(x=100, y=260, width=190)

# Coso para que no se cierre
ventana.mainloop()
