def buscar_socio(socios, codigo):
    encontrado = False
    pos = 0
    while pos < len(socios) and not encontrado:
        if socios[pos][0] == codigo:
            encontrado = True
        else:
            pos += 1
    if not encontrado:
        pos = -1
    return pos

def consultar(socios):
    print("CONSULTAR SOCIO")
    print()
    print("Indique el registro a consultar: ", end= "")
    registro= validar_positivo()   
    pos = buscar_socio(socios, registro)
    socio_consultado = []
        
    if pos !=-1 :
        socio_consultado.append(socios[pos])
        mostrar_socios(socio_consultado)
    else:
        print("El registro", registro, "no existe")


def dar_alta(socios, actividades):
    print("ALTA DE SOCIO")
    print()
    codigo_maximo = 0
    for socio in socios:
        if socio[0] > codigo_maximo:
            codigo_maximo = socio[0]
    codigo = codigo_maximo + 1

    nombre = validar_texto("Nombre del socio: ")
    nombre_actividad= seleccionar_actividad(actividades)

    print("Ingrese el valor de la cuota:", end=" ")
    valor_cuota = validar_positivo()
    print()

    estado = "activo"

    socio = [codigo, nombre, nombre_actividad, valor_cuota, estado]
    socios.append(socio)

    print("¡Socio registrado con éxito!")
    print(socio)