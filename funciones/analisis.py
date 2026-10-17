
def longitud_texto(texto):
    longitud = len(texto)
    return longitud

def cantidad_palabras(texto):
    texto_normal = normalizar_texto(texto)
    palabras = separar_palabras(texto_normal)
    cantidad = len(palabras)
    return cantidad

def contar_termino(termino, texto):
    return texto.lower().count(termino.lower())

