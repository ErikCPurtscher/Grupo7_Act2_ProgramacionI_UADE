
def pedir_entero_positivo(mensaje):
    """Pide un entero mayor o igual a 0 y lo devuelve. Reintenta ante texto o negativos."""
    valido = False
    while not valido:
        try:
            numero = int(input(mensaje).strip())
            if numero < 0:
                raise ValueError("El número no puede ser negativo.")
            valido = True
        except ValueError as error:
            print(f'Error: {error}')
            print("Debe ingresar un número entero positivo.")
        else:
            return numero

def validar_rango(valor, minimo, maximo):
    """Lanza ValueError si el valor está fuera del rango [minimo, maximo]."""
    if valor < minimo or valor > maximo:
        raise ValueError(f"El valor debe estar entre {minimo} y {maximo}.")         


def pedir_entero_en_rango(mensaje, minimo, maximo):
    """Pide un entero y lo devuelve solo si está entre minimo y maximo; si no, reintenta."""
    valido = False
    while not valido:
        valor = pedir_entero_positivo(mensaje)
        try:
            validar_rango(valor, minimo, maximo)
            valido = True
        except ValueError as error:
            print(f"Error: {error}")
    return valor       

def pedir_cadena_validada(mensaje, min_long, max_long, sin_espacios, no_solo_numeros):
    """Pide un texto y valida vacío, longitud y caracteres. Reintenta hasta que sea válido."""
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

def pedir_caracter_en_posicion(texto):
    """Pide una posición (positiva o negativa) y devuelve el carácter del texto
    en ella. Distingue un valor no numérico (ValueError) de una posición fuera
    del texto (IndexError) y reintenta hasta que el ingreso sea válido."""
    recuperado = False
    while not recuperado:
        try:
            posicion = int(input(f"Posición del carácter (0 a {len(texto) - 1}, o negativa): ").strip())
            caracter = texto[posicion]
        except ValueError:
            print("Error: la posición debe ser un número entero.")
        except IndexError as error:
            print(f"Error: la posición está fuera del texto ({error}).")
        else:
            recuperado = True
    return caracter
