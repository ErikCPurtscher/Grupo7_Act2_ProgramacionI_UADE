def pedir_entero(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
        except ValueError:
            print("Error: debe ingresar un número entero.")
        else:
            try:
                validar_rango(valor, minimo, maximo)
                return valor
            except ValueError as error:
                print(f"Error: {error}")


def validar_rango(valor, minimo, maximo):
    if valor < minimo or valor > maximo:
        raise ValueError(f"el valor debe estar entre {minimo} y {maximo}.")                