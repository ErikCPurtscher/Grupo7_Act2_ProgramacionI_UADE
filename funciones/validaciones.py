def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje).strip()
        try:
            return int(entrada)
        except ValueError:
            print("Error: debe ingresar un número entero.")

def validar_rango(valor, minimo, maximo):
    if valor < minimo or valor > maximo:
        raise ValueError(f"El valor debe estar entre {minimo} y {maximo}.")         


def pedir_entero_en_rango(mensaje, minimo, maximo):
    valido = False
    while not valido:
        valor = pedir_entero(mensaje)
        try:
            validar_rango(valor, minimo, maximo)
            valido = True
        except ValueError as error:
            print(f"Error: {error}")
    return valor       

def pedir_cadena_validada(mensaje, min_long, max_long, sin_espacios, no_solo_numeros):

    while True:
        entrada = input(mensaje).strip()
        try:
            if len(entrada) == 0:
                raise ValueError("El campo no puede estar vacío.")
            if len(entrada) < min_long:
                raise ValueError(f"El texto debe tener al menos {min_long} caracteres.")
            if len(entrada) > max_long:
                raise ValueError(f"El texto no debe superar los {max_long} caracteres.")
            if sin_espacios and " " in entrada:
                raise ValueError("El texto no puede contener espacios.")
            if no_solo_numeros and entrada.isdigit():
                raise ValueError("El texto no puede contener solo números.")        
        except ValueError as error:
            print(f"Error de validación: {error}")
        else:
            return entrada