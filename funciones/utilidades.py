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