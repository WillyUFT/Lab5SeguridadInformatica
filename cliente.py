import socket

def clientePrograma():
    host = socket.gethostname()
    port = 5000

    clientSocket = socket.socket()
    clientSocket.connect((host, port))

    clientSocket.send()
    data = clientSocket.recv(1024).decode()

    print('El servidor dijo: ' + data)
    clientSocket.close()

if __name__ == '__main__':
    clientePrograma()