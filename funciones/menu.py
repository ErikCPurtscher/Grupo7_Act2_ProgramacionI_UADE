from funciones.validaciones import pedir_entero_en_rango, pedir_cadena_validada
from datos import TEXTO
from .procesamiento import ingresar_registro, normalizar_texto, separar_palabras
from .procesamiento import procesar_palabras, reconstruir_texto
from .analisis import analizar_contenido
from .utilidades import consultar_registro


def mostrar_menu():
    print("\n" + "=" * 52)
    print("   SISTEMA DE ANÁLISIS DE RESEÑAS")
    print("=" * 52)
    print("1. Ingresar Registro")
    print("2. Normalizar el texto")
    print("3. Analizar el contenido")
    print("4. Procesar palabras y reconstruir el texto")
    print("5. Reemplazar y extraer información")
    print("6. Transformacion mediante codigos de caracteres")
    print("7. Generar reporte de análisis")
    print("8. Manejar errores y permitir recuperacion")
    print("0. Salir")

def opcion_normalizar(matriz):
    registro = consultar_registro(matriz)
    if registro is not None:
        print(f"\nOriginal:    '{registro[TEXTO]}'")
        print(f"Normalizado: '{normalizar_texto(registro[TEXTO])}'")

def opcion_analizar(matriz):
    registro = consultar_registro(matriz)
    if registro is not None:
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
    registro = consultar_registro(matriz)
    if registro is not None:
        palabras = separar_palabras(normalizar_texto(registro[TEXTO]))
        nuevo_texto = reconstruir_texto(procesar_palabras(palabras))
        print(f"\nOriginal:  '{registro[TEXTO].strip()}'")
        print(f"Procesado: '{nuevo_texto}'")

def ejecutar_opcion(opcion, matriz):
   
    if opcion == 1:
        ingresar_registro(matriz)
    elif opcion == 2:
        opcion_normalizar(matriz)
    elif opcion == 3:
        opcion_analizar(matriz)
    elif opcion == 4:
        opcion_procesar_palabras(matriz)
    elif opcion == 5:
        print("reemplazar_extraer(matriz)")
    elif opcion == 6:
        print("transformar(matriz)")
    elif opcion == 7:
        print("")
    elif opcion == 8:
        print("permitir_recuperar(matriz)")
 
 
def iniciar_menu(matriz):
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = pedir_entero_en_rango("Elija una opción: ", 0, 8)
        try:
            ejecutar_opcion(opcion, matriz)
        finally:
            if opcion != 0:
                input("\nPresione ENTER para volver al menú...")
    print("\n¡Hasta luego!")
