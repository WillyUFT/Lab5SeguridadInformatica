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
# Importamos los cifrados
import cifrados

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

mensajeEntradaTxt = "mensajeentrada.txt"

# Función para leer el txt, encriptarlo y descriptarlo con DES
def txt_des():
    # Si es que mandamos las variables y están buenas
    if puedeLeerTexto:
        # leemos el txt de entrada
        mensajeEntrada = leer.leer_texto(mensajeEntradaTxt)
        # nonce es como un número aleatorio, el mensaje es el resultado
        nonce, mensajeEncriptado, tag = cifrados.encriptar_des(mensajeEntrada)
        # Mensaje desencriptado.
        mensajeDesencriptado = cifrados.desencriptar_des(nonce, mensajeEncriptado, tag)
        # Mensaje que vamos a mostrar en pantalla
        textoFinal = (
            "Encriptación mediante DES\nMensaje de entrada: "
            + str(mensajeEntrada)
            + "\nTexto encriptado: "
            + str(mensajeEncriptado)
            + "\nTexto Desencriptado: "
            + str(mensajeDesencriptado)
        )
        # Lo escribimos en el texto de salida.
        leer.escribir_texto_salida(textoFinal)
        # Borramos todo lo que estaba en la ventana
        mensajeTxt.delete("1.0", "end")
        # Lo mostramos en pantalla
        mensajeTxt.insert("end", textoFinal)


# Función para leer el txt, encriptarlo y descriptarlo con 3DES
def txt_3des():
    # Si es que mandamos las variables y están buenas.
    if puedeLeerTexto:
        # leemos el txt de entrada
        mensajeEntrada = leer.leer_texto(mensajeEntradaTxt)
        # nonce es como un número aleatorio, el mensaje es el resultado
        nonce, mensajeEncriptado = cifrados.encriptar_3des(mensajeEntrada)
        # Mensaje desencriptado.
        mensajeDesencriptado = cifrados.desencriptar_3des(nonce, mensajeEncriptado)
        # Mensaje que vamos a mostrar en pantalla
        textoFinal = (
            "Encriptación mediante 3DES\nMensaje de entrada: "
            + str(mensajeEntrada)
            + "\nTexto encriptado: "
            + str(mensajeEncriptado)
            + "\nTexto Desencriptado: "
            + str(mensajeDesencriptado)
        )
        # Lo escribimos en el texto de salida.
        leer.escribir_texto_salida(textoFinal)
        # Borramos todo lo que estaba en la ventana
        mensajeTxt.delete("1.0", "end")
        # Lo mostramos en pantalla
        mensajeTxt.insert("end", textoFinal)


# función para leer el txt, encriptarlo y descriptarlo con AES
def txt_aes():
    # Si es que mandamos las variables y están buenas
    if puedeLeerTexto:
        # leemos el txt de entrada
        mensajeEntrada = leer.leer_texto(mensajeEntradaTxt)
        # nonce es como un número aleatorio, el mensaje es el resultado
        nonce, mensajeEncriptado, tag = cifrados.encriptar_aes(mensajeEntrada)
        # Mensaje desencriptado.
        mensajeDesencriptado = cifrados.desencriptar_aes(nonce, mensajeEncriptado, tag)
        # Mensaje que vamos a mostrar en pantalla
        textoFinal = (
            "Encriptación mediante AES\nMensaje de entrada: "
            + str(mensajeEntrada)
            + "\nTexto encriptado: "
            + str(mensajeEncriptado)
            + "\nTexto Desencriptado: "
            + str(mensajeDesencriptado)
        )
        # Lo escribimos en el texto de salida.
        leer.escribir_texto_salida(textoFinal)
        # Borramos todo lo que estaba en la ventana
        mensajeTxt.delete("1.0", "end")
        # Lo mostramos en pantalla
        mensajeTxt.insert("end", textoFinal)

# Función para insertar log a la interfaz
def insertar_log(listaLogs):
    # Vamos insertando uno a uno los logs.
    # Se borra lo que pueda estar escrito en la casilla de las interacciones
    interacciónClienteServidor.delete("1.0", "end")
    for log in listaLogs:
        # Se escribe en la casilla de mensaje el resultado
        interacciónClienteServidor.insert("end", log + "\n")


# Función para enviar datos al servidor.
def enviar_datos(AoK, p, g, BoK):
    listaDatos = [AoK, p, g, BoK]
    data = pickle.dumps(listaDatos)
    client.send(data)


# Función para enviar variables desde el cliente al servidor.
def enviar_variables():
    # Primero se valida que las variables sean valores numéricos.
    if ValCal.letras_chiquitas_numericas(
        aChiquita.get(), gChiquita.get(), pChiquita.get()
    ):
        # Se transforman de string a int
        achiquitaNumero = int(aChiquita.get())
        gchiquitaNumero = int(gChiquita.get())
        pchiquitaNumero = int(pChiquita.get())

        # Validamos que sean números enteros y las validaciónes generales que son
        # P debe ser un número primo
        # a debe ser un número entre 0 y P-1
        # g debe ser un número entre 0 y P
        if ValCal.letras_chiquitas_enteras(
            achiquitaNumero, gchiquitaNumero, pchiquitaNumero
        ) and ValCal.validaciones_variables_cliente(
            achiquitaNumero, pchiquitaNumero, gchiquitaNumero
        ):
            # Listado de los logs
            listaLogs = []
            # Calculamos la A del cliente.
            Acliente = ValCal.calcular_a_o_b(
                gchiquitaNumero, achiquitaNumero, pchiquitaNumero
            )
            # Añadimos a la lista de logs
            listaLogs.append("El cliente le envió al servidor, A = " + str(Acliente))
            # Enviamos el A para que el servidor calcule el B
            enviar_datos(Acliente, pchiquitaNumero, gchiquitaNumero, "B")
            # Recogemos el B del servidor.
            BServidor = int(client.recv(1024).decode())
            # Añadimos a la lista de logs
            listaLogs.append("El servidor le envió al cliente, B = " + str(BServidor))
            # Calculamos K del cliente
            Kcliente = ValCal.calcular_k(BServidor, achiquitaNumero, pchiquitaNumero)
            # Añadimos a la lista de logs
            listaLogs.append("El cliente le envió al servidor, K = " + str(Kcliente))
            # Enviamos los mismos datos, pero ahora queremos calcular la K del servidor.
            enviar_datos(Acliente, pchiquitaNumero, gchiquitaNumero, "K")
            # Recogemos la K del servidor.
            Kserver = int(client.recv(1024).decode())
            # Añadimos a la lista de logs
            listaLogs.append("El servidor le envió al cliente, K = " + str(Kserver))
            # Mandamos los logs.
            insertar_log(listaLogs)
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
interacciónClienteServidorLabel = TK.Label(ventana, text="Interacción cliente/servidor")
interacciónClienteServidorLabel.place(x=650, y=50, width=330)

# Acá se pondrá el log entre el cliente y el servidor.
interacciónClienteServidor = TK.Text(ventana)
interacciónClienteServidor.place(x=650, y=70, width=330, height=125)

# Este es el cosito que dice mensaje txt
mensajeTxtLabel = TK.Label(ventana, text="Mensaje")
mensajeTxtLabel.place(x=650, y=225, width=330)

# Acá se pondrá el log entre el cliente y el servidor.
mensajeTxt = TK.Text(ventana)
mensajeTxt.place(x=650, y=245, width=330, height=125)

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
TK.Button(ventana, text="Enviar variables", command=lambda: enviar_variables()).place(
    x=100, y=230, width=190
)

# Boton para mandar encriptar el archivo txt de entrada con des
TK.Button(
    ventana,
    text="Encriptar txt de entrada con DES",
    command=lambda: txt_des(),
).place(x=100, y=260, width=190)

# Boton para mandar encriptar el archivo txt de entrada con 3des
TK.Button(
    ventana,
    text="Encriptar txt de entrada con 3DES",
    command=lambda: txt_3des(),
).place(x=100, y=290, width=190)

# Boton para mandar encriptar el archivo txt de entrada con 3des
TK.Button(
    ventana,
    text="Encriptar txt de entrada con AES",
    command=lambda: txt_aes(),
).place(x=100, y=320, width=190)

# Coso para que no se cierre
ventana.mainloop()
