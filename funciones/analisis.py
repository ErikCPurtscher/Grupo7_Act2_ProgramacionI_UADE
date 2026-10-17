from .procesamiento import procesar_palabras

def longitud_texto(texto):
    longitud = len(texto)
    return longitud

def cantidad_palabras(palabras):
    texto_normal = normalizar_texto(texto)
    palabras = procesar_palabras(texto_normal)
    cantidad = len(palabras)
    return cantidad

def contar_expreson(expresion, texto):
    return texto.lower().count(expresion.lower())

def verificar_existencia(expresion, texto):
    existe_expresion = expresion in texto
    return existe_expresion

def analizar_contenido(texto):
    texto_normal = normalizar_texto(texto)
    palabras = procesar_palabras(texto_normal)

    longitud = longitud_texto(texto_normal)
    
