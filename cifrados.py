# Importamos la librería del hash
import hashlib as hl
# Importamos la Crypto y los encriptados
from Crypto.Cipher import DES, DES3, AES
# Importamos los secretos
from secrets import token_bytes

# Cifrado rot
def rot_n(mensaje, n):
    # String mensaje
    mensajeCifrado = ""
    # En caso de que el rot indicado sea menor a 0
    if n < 0:
        n = 26 + n
    # Se recorren todos los caracteres del mensaje
    # También se deja todo el mensaje en mayúsculas
    for caracter in mensaje.upper():
        # Si el caracter es alfabético (a-z)
        if caracter.isalpha():
            # Se toma el caracter y se transforma a unicode con ord(), se le resta 65 y se le suma el n
            caracerInt = ord(caracter) - 65 + n
            # Si el caracter en unicode es mayor o igual a 26 se saca el módulo con 26 (abecedario)
            if caracerInt >= 26:
                caracerInt = caracerInt % 26
            # Ahora el unicode que obtuvimos lo cambiamos nuevamente a caracter con chr()
            caracter = chr(caracerInt + 65)
        # Agregamos el caracter al string mensaje para después mostrarlo
        mensajeCifrado += caracter
    return mensajeCifrado


# Esta es la tabla de cifrado vignere que está en el git
tabla = {}
abc = [chr(i) for i in range(65, 65 + 26)] * 2
columnas = abc[:26]
for i in range(26):
    llaveFila = abc[i]
    valoresFila = abc[i : i + 26]
    # Se crea un diccionario gigante que contiene toda la tabla de la forma A:{A:A,B:B} , etc.
    tabla[llaveFila] = dict(zip(columnas, valoresFila))

# Cifrado Vignere
def vigenere(mensaje, llave):
    # String del mensaje
    mensajeCifrado = ""
    contador = 0
    # Este while es para que en caso de que la llave sea de menor longitud que el mensaje
    # Se escriba nuevamente hasta que sea de igual o mayor longitud
    while len(llave) < len(mensaje):
        llave += llave
    # Se recorren todos los caracteres del mensaje
    # También se deja todo el mensaje en mayúsculas
    for caracter in mensaje.upper():
        # Si el caracter no es alfabético, lo agregamos al string del mensaje
        if not caracter.isalpha():
            mensajeCifrado += caracter
        # En caso contrario
        else:
            # Va tomando letra por letra la clave, en mayúsculas
            fila = llave[contador].upper()
            # Busca en la tabla la letra correspondiente y la agrega al mensaje
            mensajeCifrado += tabla[fila][caracter]
            # contador +1
            contador += 1
    return mensajeCifrado


# función para hacer el hash
def hash(mensaje):
    # Recibimos el mensaje y lo hasheamos con sha512 y codificación utf-8
    mensajeHasheado = hl.sha512(mensaje.encode("utf-8"))
    # Lo pasamos a string
    mensajeHasheadoHex = mensajeHasheado.hexdigest()
    return mensajeHasheadoHex

# Generamos key para el des
keyDes = token_bytes(8)
# Función para encriptar con DES
def encriptar_des(mensaje):
    cipher = DES.new(keyDes, DES.MODE_EAX)
    nonce = cipher.nonce
    mensajeCifrado, tag = cipher.encrypt_and_digest(mensaje.encode("ascii"))
    return nonce, mensajeCifrado, tag


# Función para desencriptar con DES
def desencriptar_des(nonce, mensajeCifrado, tag):
    cipher = DES.new(keyDes, DES.MODE_EAX, nonce=nonce)
    mensajeDescrifrado = cipher.decrypt(mensajeCifrado)
    try:
        cipher.verify(tag)
        return mensajeDescrifrado.decode("ascii")
    except:
        return False


# Generamos key para el 3des
key3Des = token_bytes(24)  # 24 bytes
# Función para encriptar con 3DES
def encriptar_3des(mensaje):
    cipher = DES3.new(key3Des, DES3.MODE_EAX)
    nonce = cipher.nonce
    mensajeCifrado = cipher.encrypt(mensaje.encode("ascii"))
    return nonce, mensajeCifrado


# Función para desencriptar con 3DES
def desencriptar_3des(nonce, mensajeCifrado):
    cipher = DES3.new(key3Des, DES3.MODE_EAX, nonce=nonce)
    mensajeDescifrado = cipher.decrypt(mensajeCifrado)
    return mensajeDescifrado.decode("ascii")


# Generamos key para el aes
keyAes = token_bytes(16)  # 16 bytes
# función para encriptar con AES
def encriptar_aes(mensaje):
    cipher = AES.new(keyAes, AES.MODE_EAX)
    nonce = cipher.nonce
    mensajeCifrado, tag = cipher.encrypt_and_digest(mensaje.encode("ascii"))
    return nonce, mensajeCifrado, tag

def desencriptar_aes(nonce, mensajeCifrado, tag):
    cipher = AES.new(keyAes, AES.MODE_EAX, nonce=nonce)
    mensajeDescifrado = cipher.decrypt(mensajeCifrado)
    try:
        cipher.verify(tag)
        return mensajeDescifrado.decode("ascii")
    except:
        return False

# Función para la red de cifrados
def red_cifrado(mensaje, password):
    # Primero ciframos el mensaje con el rot 8
    mensajeCifrado = rot_n(mensaje, 8)
    # Luego por vignere con la contraseña que le mandamos dle otro
    mensajeCifrado = vigenere(mensajeCifrado, password)
    # Luego un cifrado de rot 10, por si las moscas
    mensajeCifrado = rot_n(mensajeCifrado, 10)
    return mensajeCifrado
