# Importamos la biblioteca para la cosa del servidor y cliente.
import pickle
import socket

# Importamos las validaciones y calculos
import validacionesYCalculos

# b del servidor
b = int(input("Escoja un b, por favor: "))

# Configuramos el servidor.
port = 666  # Escojemos el puerto.
SERVER = socket.gethostbyname(socket.gethostname())  # Dirección IPv4
address = (SERVER, port)  # Dirección
format = "utf-8"  # formato en el que vamos a codificar y decodificar.

# Creamos el socket para el servidor.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hacemos el bind con la dirección
server.bind(address)

# Función para comenzar la conexión.
def comenzar_conexion():

    print("El servidor está funcionando en " + SERVER)

    server.listen()

    # Aceptar conexión y retorna una nueva conexión con el cliente.
    conn, addr = server.accept()

    while True:

        # 1024 representa la máxima cantidad de data
        # que puede ser recibida.
        # data = conn.recv(1024).decode()
        data = pickle.loads(conn.recv(1024))

        if not data:
            break

        if data[3] == "B":
            print(
                "El cliente envía:\nA = "
                + str(data[0])
                + " b = "
                + str(b)
                + " p = "
                + str(data[1])
                + " g = "
                + str(data[2])
                + " ¿Qué vamos a calcular? "
                + str(data[3])
            )

            resultado = validacionesYCalculos.calcular_a_o_b(
                int(data[2]), b, int(data[1])
            )

            conn.send(str(resultado).encode(format))
            print("El servidor envía, B = " + str(resultado))

        if data[3] == "K":
            print(
                "El cliente envía:\nA = "
                + str(data[0])
                + " b = "
                + str(b)
                + " p = "
                + str(data[1])
                + " g = "
                + str(data[2])
                + " ¿Qué vamos a calcular? "
                + str(data[3])
            )
            resultado = validacionesYCalculos.calcular_k(int(data[0]), b, int(data[1]))

            print("El servidor envía, K = " + str(resultado))

            conn.send(str(resultado).encode(format))

    conn.close()


comenzar_conexion()
