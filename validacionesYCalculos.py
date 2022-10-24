# Función para ver si un número es primo
def esPrimo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

# Función para ver si un número está entre 0 y otro


def entreCeroYOtro(g, p):
    if 0 < g and g < p:
        return True
    else:
        return False

# Función para calcular el valor de A o B


def calcularAoB(g, aob, p):
    elevacion = g**aob
    modulo = elevacion % p
    return modulo

# Función para calcular el valor de la K.


def calcularK(AoB, aob, p):
    elevacion = AoB**aob
    modulo = elevacion % p
    return modulo

# Función para ver si un caracter es numérico.


def esNumerico(n):
    if (n.isnumeric()):
        return True
    else:
        return False

# Función para ver si un número es entero.


def esEntero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False

# función para validar que a, p, y g


def validacionesVariablesCliente(a, p, g):
    botoncito = False
    if (esPrimo(p) == False):
        print("P debe ser un número primo")
    if (entreCeroYOtro(g, p) == False):
        print("g debe ser un número entre 0 y P")
    if (entreCeroYOtro(a, p-1) == False):
        print("a debe ser un número entre 0 y p-1")

    if (esPrimo(p) and
        entreCeroYOtro(g, p) and
            entreCeroYOtro(a, p-1)):
        botoncito = True
        return botoncito

# Función para validar que sean valores numéricos.


def letrasChiquitasNumericas(a, g, p):
    if(esNumerico(a) and
       esNumerico(g) and
       esNumerico(p)):
        return True
    else:
        print("Los valores deben ser números enteros")
        return False

# Función para validar que sen números enteros.


def letrasChiquitasEnteras(a, g, p):
    if(esEntero(a) and
       esEntero(g) and
       esEntero(p)):
        return True
    else:
        print("Los valores deben ser numéricos")
        return False
