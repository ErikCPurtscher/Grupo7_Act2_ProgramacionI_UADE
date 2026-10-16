from .validaciones import pedir_entero

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



def ejecutar_opcion(opcion, matriz):
   
    if opcion == 1:
        print("ingresa_registro(matriz)")
    elif opcion == 2:
        print("agregar")
    elif opcion == 3:
        print("Normalizar_texto(matriz)")
    elif opcion == 4:
        print("analizar(matriz)")
    elif opcion == 5:
        print("procesar_palabras(matriz)")
    elif opcion == 6:
        print("reemplazar_extraer(matriz)")
    elif opcion == 7:
        print("transformar(matriz)")
    elif opcion == 8:
        print("permitir_recuperar(matriz)")
 
 
def iniciar_menu(matriz):
    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = pedir_entero("Elija una opción: ", 0, 8)
        try:
            ejecutar_opcion(opcion, matriz)
        finally:
            if opcion != 0:
                input("\nPresione ENTER para volver al menú...")
    print("\n¡Hasta luego!")
