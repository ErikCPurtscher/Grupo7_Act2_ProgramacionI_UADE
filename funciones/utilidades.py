from .validaciones import pedir_entero_positivo 


def mostrar_registros(registros):
    '''Revisar formato del último campo'''
    print(f"{'Id':^8}{'Usuario':^15}{'Título':^30}{'Puntuación':^12}{'Likes':^7}{'Texto'}")
    print("-" * 350)
    for registro in registros:
        codigo = registro[0]
        usuario = registro[1]
        titulo = registro[2]
        puntaje = '*' * registro[3]
        likes = registro[4]
        texto = registro[5]
        print(f"{codigo:^8}{usuario:^15}{titulo:^30}{puntaje:^12}{likes:^7}{texto}")



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
    registro = pedir_entero_positivo("Indique el registro a consultar: ")   
    pos = buscar_registro(registros, registro)
    registro_consultado = []
    if pos !=-1 :
        registro_consultado.append(registros[pos])
        # mostrar_registros(registro_consultado)   #Para la funcion
        return registros[pos]
    else:
        print("El registro", registro, "no existe")
        return None        