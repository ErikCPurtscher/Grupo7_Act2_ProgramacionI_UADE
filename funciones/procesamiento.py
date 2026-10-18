from datos import ID, USUARIO, TITULO, TEXTO, PUNTUACION, LIKES, PUNTUACION_MIN, PUNTUACION_MAX
from .validaciones import pedir_cadena_validada,pedir_entero_en_rango, pedir_entero_positivo
from .utilidades import consultar_registro



def ingresar_registro(matriz):

    print("\n" + "=" * 54)
    print(f"{'INGRESAR NUEVO REGISTRO DE RESEÑA':^54}")
    print("=" * 54)

    if len(matriz) > 0:
        nuevo_id = matriz[-1][ID] + 1
    else:
        nuevo_id = 1

    print(f"ID asignado al nuevo registro: {nuevo_id}\n")

    usuario = pedir_cadena_validada(
        "Ingrese el nombre de usuario (mínimo 3 caracteres alfanuméricos): ",
        3,
        15,
        True,
        True
    )
    titulo = pedir_cadena_validada(
        "Ingrese el título de la película o serie: ",
        1,
        100,
        False,
        False
    )
    puntuacion = pedir_entero_en_rango(
        f"Ingrese la puntuación ({PUNTUACION_MIN} a {PUNTUACION_MAX}): ",
        minimo = PUNTUACION_MIN,
        maximo = PUNTUACION_MAX
    )
    likes = pedir_entero_positivo(
        "Ingrese la cantidad inicial de likes: ",
    )
    texto = pedir_cadena_validada(
            "Ingrese el contenido de la reseña (mínimo 5 caracteres): ",
            5,
            400,
            False,
            False
        )

    # Creación e inserción del nuevo registro
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



# def procesar_palabras(matriz):
#     registro = consultar_registro(matriz)
    
#     oraciones = registro[TEXTO]
#     palabras = oraciones.split(". ")
#     texto = ". ".join([oracion.strip().capitalize() for oracion in palabras])

#     print("texto Original:", oraciones)
#     print("Texto limpio:", texto)
#     return texto

#Nueva función para el ingreso de registro (opcion 1)

# def normalizar_texto(texto, modo="titulo"):
    
#     if not texto:
#         return ""

#     texto_limpio = texto.strip()

#     if modo == "titulo":
#         texto_normalizado = texto_limpio.title()
#     elif modo == "minusculas":
#         texto_normalizado = texto_limpio.lower()
#     elif modo == "mayusculas":
#         texto_normalizado = texto_limpio.upper()
#     elif modo == "oracion":
#         texto_normalizado = texto_limpio.capitalize()
#     else:
#         texto_normalizado = texto_limpio

#     return texto_normalizado

def normalizar_texto(texto):
    """Devuelve el texto sin espacios sobrantes (extremos y repetidos),
    en minúsculas y con la primera letra en mayúscula."""
    palabras = texto.strip().split()
    texto_limpio = " ".join(palabras).lower()
    if len(texto_limpio) > 0:
        texto_limpio = texto_limpio[0].upper() + texto_limpio[1:]
    return texto_limpio


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

