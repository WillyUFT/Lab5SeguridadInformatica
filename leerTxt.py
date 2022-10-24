# Este archivo se encarga de leer los archivos txt y compararlos

def leerTexto(archivo):
    txtEntrada = open(archivo, 'r', encoding='utf-8')
    mensajeEntrada = str(txtEntrada.read())
    txtEntrada.close()
    return mensajeEntrada


def escribirTextoSalida(texto):
    txtSalida = open('mensajeSeguro.txt', 'w', encoding='utf-8')
    txtSalida.write(texto)
    txtSalida.close()
    return texto
