from datos import ID, USUARIO, TITULO, PUNTUACION, LIKES, TEXTO, PUNTUACION_MAX
from funciones.analisis import analizar_contenido, calcular_porcentaje, promedio_puntuacion_usuario, promedio_likes_usuario
from funciones.validaciones import pedir_entero_positivo
from funciones.procesamiento import normalizar_texto


def mostrar_registros(registros):
    """Muestra en una tabla todas las reseñas de la matriz."""
    print(f"{'Id':^8}{'Usuario':^15}{'Título':^30}{'Puntuación':^12}{'Likes':^7}{'Texto'}")
    print("-" * 350)
    for registro in registros:
        codigo = registro[ID]
        usuario = registro[USUARIO]
        titulo = registro[TITULO]
        puntaje = '*' * registro[PUNTUACION]
        likes = registro[LIKES]
        texto = normalizar_texto(registro[TEXTO])
        print(f"{codigo:<8}{usuario:<15}{titulo:<30}{puntaje:<12}{likes:<7}{texto}")

def buscar_registro(registros, codigo):
    """Devuelve la posición del registro con ese ID, o -1 si no existe."""
    encontrado = False
    pos = 0
    while pos < len(registros) and not encontrado:
        if registros[pos][ID] == codigo:
            encontrado = True
        else:
            pos += 1
    if not encontrado:
        pos = -1
    return pos


def consultar_registro(registros):
    """Pide el ID de una reseña y devuelve el registro, o None si no existe."""
    print("CONSULTAR REGISTRO")
    print()
    codigo = pedir_entero_positivo("Indique el registro a consultar: ")
    pos = buscar_registro(registros, codigo)
    if pos != -1:
        registro = registros[pos]
    else:
        print("El registro", codigo, "no existe")
        registro = -1
    return registro

  ##Erik - Cambié consultar_registro para que quede un solo return al final que es algo que recomienda el profe

def generar_reporte(matriz, registro, termino, texto):
    """Muestra los datos de una reseña junto con los resultados de su análisis,
    con formato alineado y números con decimales fijos.
    'texto' es el contenido ya normalizado que se analizó."""
    longitud, palabras, apariciones, pertenece, vocales = analizar_contenido(texto, termino)
    prom_puntuacion, cant_resenias = promedio_puntuacion_usuario(matriz, registro[USUARIO])
    prom_likes, cant_likes = promedio_likes_usuario(matriz, registro[USUARIO])
    porc_vocales = calcular_porcentaje(vocales, longitud)
    porc_termino = calcular_porcentaje(apariciones * len(termino), longitud)
    if pertenece:
        respuesta = "Sí"
    else:
        respuesta = "No"

    print("\n" + "=" * 54)
    print(f"{'REPORTE DE ANÁLISIS':^54}")
    print("=" * 54)
    print(f"{'ID:':<26}{registro[ID]}")
    print(f"{'Usuario:':<26}{registro[USUARIO]}")
    print(f"{'Título:':<26}{registro[TITULO]}")
    print(f"{'Puntuación:':<26}{registro[PUNTUACION]} / {PUNTUACION_MAX}")
    print(f"{'Likes:':<26}{registro[LIKES]}")
    print(f"{'Texto:':<26}\"{texto}\"")
    print("-" * 54)
    print(f"{'Longitud del texto:':<26}{longitud} caracteres")
    print(f"{'Cantidad de palabras:':<26}{palabras}")
    print(f"{'Vocales:':<26}{vocales} ({porc_vocales:.1f}% del texto)")
    print(f"{'Término buscado:':<26}'{termino}'")
    print(f"{'Aparece en la reseña:':<26}{respuesta}")
    print(f"{'Apariciones:':<26}{apariciones} ({porc_termino:.1f}% del texto)")
    print("-" * 54)
    print(f"{'Reseñas del usuario:':<26}{cant_resenias}")
    print(f"{'Puntuación promedio:':<26}{prom_puntuacion:.2f} / {PUNTUACION_MAX}")
    print(f"{'Likes totales:':<26}{cant_likes:.1f}")
    print(f"{'Likes promedio:':<26}{prom_likes:.1f}")
    print("=" * 54)