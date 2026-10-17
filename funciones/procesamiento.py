from datos import ID, USUARIO, TITULO, TEXTO, PUNTUACION, LIKES, PUNTUACION_MIN, PUNTUACION_MAX
from .validaciones import pedir_entero, pedir_cadena_validada,pedir_entero_en_rango

def buscar_registro(registros, codigo):
    encontrado = False
    pos = 0
    while pos < len(registros) and not encontrado:
        if registros[pos][0] == codigo:
            encontrado = True
        else:
            pos += 1
    if not encontrado:
        pos = -1
    return pos

def consultar_registro(registros):
    print("CONSULTAR REGISTRO")
    print()
    print("Indique el registro a consultar: ", end= "")
    registro = validar_positivo()   
    pos = buscar_registro(registros, registro)
    registro_consultado = []
    if pos !=-1 :
        registro_consultado.append(registros[pos])
        mostrar_registros(registro_consultado)
    else:
        print("El registro", registro, "no existe")


def alta_registro(registros):
    print("ALTA DE REGISTRO")
    print()
    codigo_maximo = 0
    for registro in registros:
        if registro[0] > codigo_maximo:
            codigo_maximo = socio[0]
    codigo = codigo_maximo + 1

    usuario = validar_usuario("Ingrese nombre de usuario: ")
    titulo_contenido = '''Acá debería ir una función para validar y/o normalizar el nombre del contenido'''
    puntaje = pedir_entero("Ingrese un puntaje de 0 a 5: ", 0, 5)
    estado = "activo"

    socio = [codigo, nombre, nombre_actividad, valor_cuota, estado]
    socios.append(socio)

    print("¡Socio registrado con éxito!")




#Nueva función para el ingreso de registro (opcion 1)

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
    texto = pedir_cadena_validada(
        "Ingrese el contenido de la reseña (mínimo 5 caracteres): ",
        5,
        400,
        False,
        False
    )
    puntuacion = pedir_entero_en_rango(
        f"Ingrese la puntuación ({PUNTUACION_MIN} a {PUNTUACION_MAX}): ",
        minimo=PUNTUACION_MIN,
        maximo=PUNTUACION_MAX
    )
    likes = pedir_entero_en_rango(
        "Ingrese la cantidad inicial de likes (>= 0): ",
        minimo=0,
        maximo=1000000
    )

    # Creación e inserción del nuevo registro
    nuevo_registro = [nuevo_id, usuario, titulo, texto, puntuacion, likes]
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

    print(socio)