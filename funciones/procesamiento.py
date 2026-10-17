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
    print(socio)