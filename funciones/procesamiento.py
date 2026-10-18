from datos import ID, PUNTUACION_MIN, PUNTUACION_MAX
from funciones.validaciones import pedir_cadena_validada,pedir_entero_en_rango, pedir_entero_positivo

def ingresar_registro(matriz):
    """Pide los datos de una reseña, los valida y la agrega a la matriz con un nuevo ID."""
    print("\n" + "=" * 54)
    print(f"{'INGRESAR NUEVO REGISTRO DE RESEÑA':^54}")
    print("=" * 54)
    if len(matriz) > 0:
        nuevo_id = matriz[-1][ID] + 1
    else:
        nuevo_id = 1
    print(f"ID asignado al nuevo registro: {nuevo_id}\n")
    usuario = pedir_cadena_validada("Ingrese el nombre de usuario (3 a 12 caracteres alfanuméricos): ", 3, 12, True, True)
    titulo = pedir_cadena_validada("Ingrese el título de la película o serie: ", 1, 30, False, False)
    puntuacion = pedir_entero_en_rango(f"Ingrese la puntuación ({PUNTUACION_MIN} a {PUNTUACION_MAX}): ", PUNTUACION_MIN, PUNTUACION_MAX)
    likes = pedir_entero_positivo("Ingrese la cantidad inicial de likes: ")
    texto = pedir_cadena_validada("Ingrese el contenido de la reseña (mínimo 5 caracteres): ", 5, 400, False, False)
    nuevo_registro = [nuevo_id, usuario, titulo, puntuacion, likes, texto]
    matriz.append(nuevo_registro)
    print("\n" + "-" * 54)
    print(f"¡Registro #{nuevo_id} ingresado con éxito!")
    print(f"  ID:         {nuevo_id}")
    print(f"  Usuario:    {usuario}")
    print(f"  Título:     {titulo}")
    print(f"  Texto:      \"{texto}\"")
    print(f"  Puntuación: {puntuacion} / {PUNTUACION_MAX}")
    print(f"  Likes:      {likes}")
    print("-" * 54)


def normalizar_texto(texto):
    """Devuelve el texto sin espacios sobrantes, en minúsculas y con la primera
    letra de cada oración en mayúscula (después de punto, dos puntos, ! o ?)."""
    palabras = texto.strip().lower().split()
    resultado = []
    inicio_oracion = True
    for palabra in palabras:
        if inicio_oracion:
            if palabra[0] == "¡" or palabra[0] == "¿":
                palabra = palabra[0] + palabra[1:].capitalize()
            else:
                palabra = palabra.capitalize()
        resultado.append(palabra)
        ultimo = palabra[-1]
        inicio_oracion = ultimo == "." or ultimo == "!" or ultimo == "?" or ultimo == ":"
    return " ".join(resultado)


def separar_palabras(texto):
    """Devuelve la lista de palabras de un texto."""
    return texto.split()


def procesar_palabras(palabras):
    """Recorre una lista de palabras expandiendo las abreviaturas habituales
    en reseñas ("q", "xq") y censurando la palabra "spoiler".
    Devuelve la nueva lista, conservando los signos de puntuación."""
    resultado = []
    for palabra in palabras:
        base = palabra.lower().strip(".,;:!?¿¡")
        if base == "q":
            resultado.append(palabra.lower().replace("q", "que"))
        elif base == "xq":
            resultado.append(palabra.lower().replace("xq", "porque"))
        elif base == "spoiler":
            resultado.append(palabra.lower().replace("spoiler", "[SPOILER]"))
        else:
            resultado.append(palabra)
    return resultado


def reconstruir_texto(palabras):
    """Une una lista de palabras en una sola cadena separada por espacios."""
    return " ".join(palabras)

def reemplazar_texto(texto, buscado, nuevo):
    """Reemplaza todas las apariciones de 'buscado' por 'nuevo'
    (distingue mayúsculas de minúsculas)."""
    return texto.replace(buscado, nuevo)


def extraer_fragmentos(texto, cantidad):
    """Devuelve los primeros y los últimos 'cantidad' caracteres del texto
    y el texto completo invertido (slicing con índice negativo y con paso)."""
    inicio = texto[:cantidad]
    final = texto[-cantidad:]
    invertido = texto[::-1]
    return inicio, final, invertido

def codificar_texto(texto, desplazamiento):
    """Desplaza el código de cada carácter con ord() y chr().
    Para decodificar se usa el mismo desplazamiento con signo negativo."""
    resultado = ""
    for caracter in texto:
        resultado += chr(ord(caracter) + desplazamiento)
    return resultado