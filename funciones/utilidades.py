def mostrar_registros(registros):
    print(f"{'Reseña':^8}{'Título':<30}{'Precio':>12}")
    print("-" * 52)
    for producto in productos:
        codigo = producto[0]
        descripcion = producto[1]
        precio = producto[2]
        print(f"{codigo:<10}{descripcion:<30}${precio:>11.2f}"