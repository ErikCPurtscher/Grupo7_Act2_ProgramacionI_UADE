from funciones.validaciones import pedir_entero_en_rango
from funciones.procesamiento import ingresar_registro
from funciones.utilidades import mostrar_registros
from funciones.opciones_menu import opcion_analizar, opcion_codificar, opcion_normalizar, opcion_procesar_palabras, opcion_reemplazar_extraer, opcion_reporte


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
    print("8. Ver todas las reseñas")
    print("0. Salir")

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
        opcion_reemplazar_extraer(matriz)
    elif opcion == 6:
        opcion_codificar(matriz)
    elif opcion == 7:
        opcion_reporte(matriz)
    elif opcion == 8:
        mostrar_registros(matriz)
 
 
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
