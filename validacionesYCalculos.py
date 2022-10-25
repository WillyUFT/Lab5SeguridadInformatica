# Función para ver si un número es primo
def es_primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


# Función para ver si un número está entre 0 y otro
def entre_cero_y_otro(g, p):
    if 0 < g and g < p:
        return True
    else:
        return False


# Función para calcular el valor de A o B
def calcular_a_o_b(g, aob, p):
    elevacion = g**aob
    modulo = elevacion % p
    return modulo


# Función para calcular el valor de la K.
def calcular_k(AoB, aob, p):
    elevacion = AoB**aob
    modulo = elevacion % p
    return modulo


# Función para ver si un caracter es numérico.
def es_numerico(n):
    if n.isnumeric():
        return True
    else:
        return False


# Función para ver si un número es entero.
def es_entero(n):
    if isinstance(n, int):
        return True
    else:
        return False


# función para validar que a, p, y g
def validaciones_variables_cliente(a, p, g):
    botoncito = False
    if es_primo(p) == False:
        print("P debe ser un número primo")
    if entre_cero_y_otro(g, p) == False:
        print("g debe ser un número entre 0 y P")
    if entre_cero_y_otro(a, p - 1) == False:
        print("a debe ser un número entre 0 y p-1")
    if es_primo(p) and entre_cero_y_otro(g, p) and entre_cero_y_otro(a, p - 1):
        botoncito = True
        return botoncito


# Función para validar que sean valores numéricos.
def letras_chiquitas_numericas(a, g, p):
    if es_numerico(a) and es_numerico(g) and es_numerico(p):
        return True
    else:
        print("Los valores deben ser números enteros")
        return False


# Función para validar que sen números enteros.
def letras_chiquitas_enteras(a, g, p):
    if es_entero(a) and es_entero(g) and es_entero(p):
        return True
    else:
        print("Los valores deben ser numéricos")
        return False
