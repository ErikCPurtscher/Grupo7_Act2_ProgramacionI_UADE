from datos import TITULO, PUNTUACION


def longitud_texto(texto):
    """Devuelve la cantidad de caracteres del texto."""
    longitud = len(texto)
    return longitud


def cantidad_palabras(texto):
    """Devuelve la cantidad de palabras del texto (ignora espacios repetidos)."""
    palabras = texto.split()
    return len(palabras)


def contar_expreson(expresion, texto):
    """Cuenta las apariciones de la expresión en el texto, sin distinguir mayúsculas."""
    return texto.lower().count(expresion.lower())


def verificar_existencia(expresion, texto):
    """Indica si la expresión está en el texto, sin distinguir mayúsculas."""
    existe_expresion = expresion.lower() in texto.lower()
    return existe_expresion


def contar_vocales(texto):
    """Recorre el texto carácter por carácter y cuenta las vocales (con y sin tilde)."""
    cantidad = 0
    for caracter in texto.lower():
        if caracter in "aeiouáéíóúü":
            cantidad += 1
    return cantidad


def analizar_contenido(texto, termino):
    """Calcula longitud, cantidad de palabras, apariciones del término,
    si el término pertenece al texto y cantidad de vocales.
    Devuelve los cinco valores en ese orden."""
    longitud = longitud_texto(texto)
    palabras = cantidad_palabras(texto)
    apariciones = contar_expreson(termino, texto)
    pertenece = verificar_existencia(termino, texto)
    vocales = contar_vocales(texto)
    return longitud, palabras, apariciones, pertenece, vocales


def calcular_porcentaje(parte, total):
    """Devuelve 'parte' como porcentaje de 'total' (0 si el total es cero)."""
    try:
        porcentaje = parte / total * 100
    except ZeroDivisionError:
        porcentaje = 0
    return porcentaje


def promedio_puntuacion_titulo(matriz, titulo):
    """Devuelve el promedio de puntuación y la cantidad de reseñas de un título
    (promedio 0 si el título no tiene reseñas)."""
    suma = 0
    cantidad = 0
    for registro in matriz:
        if registro[TITULO] == titulo:
            suma += registro[PUNTUACION]
            cantidad += 1
    try:
        promedio = suma / cantidad
    except ZeroDivisionError:
        promedio = 0
    return promedio, cantidad