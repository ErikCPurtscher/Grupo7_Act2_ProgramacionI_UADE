from funciones.menu import iniciar_menu
from datos import resenias

 
 
def main():
    """Inicia el sistema de análisis de reseñas con los datos precargados."""
    print("Bienvenido al sistema.")
    iniciar_menu(resenias)
 
 
main()
 