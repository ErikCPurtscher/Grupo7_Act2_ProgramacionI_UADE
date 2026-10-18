from datos import TEXTO
from funciones.validaciones import pedir_entero_en_rango, pedir_cadena_validada, pedir_caracter_en_posicion
from funciones.procesamiento import normalizar_texto, separar_palabras, procesar_palabras, reconstruir_texto, reemplazar_texto, extraer_fragmentos, codificar_texto
from funciones.analisis import analizar_contenido
from funciones.utilidades import consultar_registro, generar_reporte


def opcion_normalizar(matriz):
    pos = consultar_registro(matriz)
    if pos != -1:
        registro = matriz[pos]
        print(f"\nOriginal:    '{registro[TEXTO]}'")
        print(f"Normalizado: '{normalizar_texto(registro[TEXTO])}'")

def opcion_analizar(matriz):
    pos = consultar_registro(matriz)
    if pos != -1:
        registro = matriz[pos]
        texto = normalizar_texto(registro[TEXTO])
        termino = pedir_cadena_validada("Carácter o término a buscar: ", 1, 30, False, False)
        longitud, palabras, apariciones, pertenece, vocales = analizar_contenido(texto, termino)
        print(f"\nLongitud del texto:   {longitud} caracteres")
        print(f"Cantidad de palabras: {palabras}")
        print(f"Vocales:              {vocales}")
        print(f"Apariciones de '{termino}': {apariciones}")
        if pertenece:
            print(f"'{termino}' pertenece al texto.")
        else:
            print(f"'{termino}' NO pertenece al texto.")

def opcion_procesar_palabras(matriz):
    pos = consultar_registro(matriz)
    if pos != -1:
        registro = matriz[pos]
        palabras = separar_palabras(normalizar_texto(registro[TEXTO]))
        nuevo_texto = reconstruir_texto(procesar_palabras(palabras))
        print(f"\nOriginal:  '{registro[TEXTO].strip()}'")
        print(f"Procesado: '{nuevo_texto}'")

def opcion_reemplazar_extraer(matriz):
    pos = consultar_registro(matriz)
    if pos != -1:
        registro = matriz[pos]
        texto = normalizar_texto(registro[TEXTO])
        print(f"\nTexto: '{texto}'")

        buscado = pedir_cadena_validada("Texto a reemplazar: ", 1, 30, False, False)
        nuevo = pedir_cadena_validada("Reemplazar por: ", 1, 30, False, False)
        print(f"Resultado: '{reemplazar_texto(texto, buscado, nuevo)}'")

        cantidad = pedir_entero_en_rango("\nCantidad de caracteres a extraer: ", 1, len(texto))
        inicio, final, invertido = extraer_fragmentos(texto, cantidad)
        print(f"Primeros {cantidad}: '{inicio}'")
        print(f"Últimos {cantidad}:  '{final}'")
        print(f"Invertido:  '{invertido}'")

        caracter = pedir_caracter_en_posicion(texto)
        print(f"Carácter elegido: '{caracter}'")

def opcion_codificar(matriz):
    pos = consultar_registro(matriz)
    if pos != -1:
        registro = matriz[pos]
        texto = normalizar_texto(registro[TEXTO])
        desplazamiento = pedir_entero_en_rango("Desplazamiento (1 a 4): ", 1, 4)
        codificado = codificar_texto(texto, desplazamiento)
        decodificado = codificar_texto(codificado, -desplazamiento)
        print(f"\nOriginal:     '{texto}'")
        print(f"Codificado:   '{codificado}'")
        print(f"Decodificado: '{decodificado}'")

def opcion_reporte(matriz):
    pos = consultar_registro(matriz)
    if pos != -1:
        registro = matriz[pos]
        texto = normalizar_texto(registro[TEXTO])
        termino = pedir_cadena_validada("Carácter o término a buscar: ", 1, 30, False, False)
        generar_reporte(matriz, registro, termino, texto)
