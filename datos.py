"""Datos iniciales del sistema de reseñas de películas y series."""
 
# Posición de cada columna dentro de un registro
ID = 0
USUARIO = 1
TITULO = 2
TEXTO = 3
PUNTUACION = 4
LIKES = 5
 
# Rango válido de puntuación (entera, estilo estrellas)
PUNTUACION_MIN = 0
PUNTUACION_MAX = 5
 
# ---------------------------------------------------------------------------
# CASOS DE PRUEBA INCLUIDOS EN LOS DATOS (referencia por ID de reseña)
# ---------------------------------------------------------------------------
# Normalización:
#   - Espacios sobrantes en los extremos: 2, 7, 9, 16, 17, 20, 22, 25, 29,
#     32, 37, 45, 47, 50
#   - Espacios dobles o triples entre palabras: 7, 30
#     (split() sin argumentos vs. split(" ") dan resultados distintos)
#   - Texto completo en mayúsculas: 3, 29
#   - Mayúsculas mezcladas dentro del texto: 16, 37, 40, 47
#   - Texto que empieza en minúscula: 7, 9, 12, 20, 25, 27, 30, 37, 42, 47, 50
#   - Nombres propios en minúscula: 9 (michael scott), 12 (francia),
#     20 (batman, superman), 42 (abba)
#
# Procesamiento de palabras y replace():
#   - Abreviatura "q": 7, 12, 30, 47, 50
#   - Abreviatura "xq": 20
#   - Errores de ortografía:
#       b/v  -> 7 (debuelva), 17 (bi, beria), 32 (Bestuario), 47 (BEAN), 50 (bi)
#       h    -> 12 y 40 (ay), 32 (ermoso)
#       c/s  -> 25 (demaciado), 50 (esplica)
#       otros-> 17 (trajica), 25 (aver)
#   - Tildes faltantes: 12, 17, 25, 37, 40, 42
#   - Palabra "spoiler" (para censurar): 5, 13, 23, 33, 43
#     (el 5 la tiene dos veces: "Spoiler" y "spoiler" -> sensible a mayúsculas)
#   - Signos repetidos: 12 y 37 (...), 17 (!!!), 42 (!!)
#
# Análisis (count / in):
#   - Palabras repetidas: 7 (muy, larga), 10 (oscura), 17 (diez, veces),
#     22 (pegadiza), 27 (mala x3), 37 (llore x3), 40 (autos, espacio)
#   - Textos más largos (útiles para slicing con paso o negativo): 1, 4, 5, 25
#   - Números dentro del texto: 7 (2 horas), 26 (2000)
#
# Transformación con ord() / chr():
#   - Vocales con tilde y ñ: muchos registros (ej. 37 "pañuelos")
#   - Signos de apertura ¿ ¡: 15, 36
#
# Estadísticas y reporte:
#   - 10 usuarios con 5 reseñas cada uno (ranking y promedios por usuario)
#   - Títulos repetidos: Cats (7, 50), Breaking Bad (3, 49),
#     Relatos salvajes (6, 48)
#   - Reseñas con 0 likes: 22, 39, 50
#   - Reseñas con puntuación 0: 27, 50
#   - Títulos con números o signos: 2, 4, 28, 40
#   - Usuario con mayúsculas: GuilleCine (8, 18, 28, 38, 48)
# ---------------------------------------------------------------------------
 
# Matriz de reseñas: [id, usuario, titulo, texto, puntuacion, likes]
resenias = [
    [1, "cinefilo92", "El Padrino", "Una obra maestra del cine. La actuación de Marlon Brando es inolvidable y la música acompaña cada escena.", 5, 342],
    [2, "lauramovies", "Toy Story 3", "   Me hizo llorar como a una nena. Pixar sabe tocar el corazón de grandes y chicos.   ", 5, 128],
    [3, "popcorn88", "Breaking Bad", "LA MEJOR SERIE DE LA HISTORIA. NO HAY DISCUSIÓN.", 5, 512],
    [4, "nachocritico", "Avatar: El camino del agua", "Visualmente impresionante, pero el guion es flojo. Mucho efecto y poca historia, mucho ruido y pocas nueces.", 3, 87],
    [5, "seriefan", "Stranger Things", "Spoiler: Eleven vuelve a salvar a todos. La temporada es buena, pero el spoiler del final me lo arruinaron en redes.", 4, 64],
    [6, "martintv", "Relatos salvajes", "Humor negro argentino en su máxima expresión. Cada relato es mejor que el anterior.", 5, 203],
    [7, "sofi2000", "Cats", "    no la recomiendo. aburrida,  rara  y larga. muy, muy larga. q alguien me debuelva las 2 horas    ", 1, 15],
    [8, "GuilleCine", "El secreto de sus ojos", "Ricardo Darín está brillante. La escena del estadio es una de las mejores del cine argentino.", 5, 276],
    [9, "anaflix", "The Office", "  divertida, incómoda y entrañable. michael scott es un personaje único.  ", 4, 98],
    [10, "tomasreview", "Joker", "Una actuación enorme de Joaquin Phoenix. La película es oscura, oscura de verdad, y no es para todos.", 4, 154],
    [11, "cinefilo92", "Interestelar", "Ciencia y emoción en partes iguales. La banda sonora de Hans Zimmer es épica.", 5, 301],
    [12, "lauramovies", "Emily en París", "linda para pasar el rato aunque los cliches sobre francia cansan un poco... ay capitulos q son iguales", 3, 22],
    [13, "popcorn88", "Game of Thrones", "Siete temporadas geniales y una octava para el olvido. Spoiler: el final decepciona.", 2, 445],
    [14, "nachocritico", "Oppenheimer", "Larga pero atrapante. Nolan vuelve a jugar con el tiempo y la narrativa.", 4, 190],
    [15, "seriefan", "Dark", "¿Quién es quién? ¿Cuándo pasa qué? Hay que verla con un cuaderno al lado, pero vale la pena.", 5, 167],
    [16, "martintv", "Los Simuladores", "   CLÁSICO de la televisión argentina. Santos, Medina, Lamponne y Ravenna son inolvidables.   ", 5, 133],
    [17, "sofi2000", "Titanic", "  Romantica y trajica. La bi diez veces y la beria diez veces mas!!!  ", 4, 58],
    [18, "GuilleCine", "Nueve reinas", "Un guion perfecto. Nunca sabés quién engaña a quién hasta el final.", 5, 141],
    [19, "anaflix", "Black Mirror", "Algunos capítulos son geniales y otros no tanto. La tecnología como espejo de lo peor de nosotros.", 4, 76],
    [20, "tomasreview", "Batman v Superman", "   mucho ruido poca historia xq ni batman ni superman se salvan de un guion confuso   ", 2, 9],
    [21, "cinefilo92", "Ciudad de Dios", "Cruda y real. Una película necesaria que no se olvida fácilmente.", 5, 188],
    [22, "lauramovies", "Frozen", "  La canción es pegadiza, demasiado pegadiza. Mis sobrinos no paran de cantarla.  ", 3, 0],
    [23, "popcorn88", "The Mandalorian", "Baby Yoda se roba cada escena. Spoiler: aparece Luke en el final de la segunda temporada.", 4, 230],
    [24, "nachocritico", "Tenet", "No entendí nada. Volví a verla y entendí un poco menos. Igual la recomiendo.", 3, 112],
    [25, "seriefan", "La casa de papel", "  las primeras partes son muy buenas, despues se estira demaciado. aver si la ultima temporada lo arregla  ", 3, 45],
    [26, "martintv", "Okupas", "Una joya del 2000. Realismo puro y personajes que se sienten reales.", 5, 97],
    [27, "sofi2000", "Crepúsculo", "mala. mala. mala. no tengo más para decir.", 0, 3],
    [28, "GuilleCine", "Argentina, 1985", "Una película importante y emocionante. La actuación de Darín y Lanzani es excelente.", 5, 389],
    [29, "anaflix", "Friends", "  NUNCA ME CANSO DE VERLA. ES MI SERIE DE CONFORT.  ", 5, 61],
    [30, "tomasreview", "Morbius", "ni el elenco la salva.   aburrida de principio a fin, no se q estaban pensando", 1, 4],
    [31, "cinefilo92", "Parásitos", "Una crítica social brillante disfrazada de thriller. Merecido el Oscar.", 5, 254],
    [32, "lauramovies", "Bridgerton", "    Bestuario ermoso y mucho drama. Ideal para un domingo de lluvia    ", 3, 18],
    [33, "popcorn88", "The Last of Us", "Spoiler: el tercer capítulo es el mejor de la serie. Bill y Frank son inolvidables.", 5, 377],
    [34, "nachocritico", "Barbie", "Más inteligente de lo que esperaba. Divertida y con un mensaje claro.", 4, 143],
    [35, "seriefan", "Merlina", "La actuación de Jenna Ortega sostiene toda la serie. El baile ya es un clásico.", 4, 89],
    [36, "martintv", "Esperando la carroza", "¡Tres empanadas! Un clásico que se ve una y otra vez y siempre da risa.", 5, 214],
    [37, "sofi2000", "Diario de una pasión", "  llore, llore y llore... MUY RECOMENDABLE para ver con pañuelos  ", 4, 37],
    [38, "GuilleCine", "El clan", "Perturbadora y bien filmada. Guillermo Francella sorprende en un papel oscuro.", 4, 122],
    [39, "anaflix", "Sex Education", "Fresca, honesta y divertida. Los personajes crecen temporada a temporada.", 4, 0],
    [40, "tomasreview", "Rápidos y furiosos 9", "AUTOS EN EL ESPACIO. si, autos en el espacio. no ay mas preguntas", 1, 31],
    [41, "cinefilo92", "Pulp Fiction", "Diálogos inolvidables y una estructura que rompe todas las reglas.", 5, 289],
    [42, "lauramovies", "Mamma Mia", "musica de abba, paisajes griegos y buena energia. imposible no cantar!!", 4, 27],
    [43, "popcorn88", "Succession", "Personajes horribles que no podés dejar de mirar. Spoiler: nadie gana.", 5, 198],
    [44, "nachocritico", "Dune", "Épica, lenta y visualmente perfecta. Hay que verla en el cine.", 4, 156],
    [45, "seriefan", "Euphoria", "   Estética increíble pero la historia a veces se pierde.   ", 3, 52],
    [46, "martintv", "Casados con hijos", "Pepe Argento es un personaje eterno. La repiten y la vuelvo a ver.", 4, 79],
    [47, "sofi2000", "Sharknado", "  tan mala q es buena. o no. definitivamente no. NO LA BEAN  ", 1, 12],
    [48, "GuilleCine", "Relatos salvajes", "El episodio de la boda es mi favorito. Erica Rivas está espectacular.", 5, 167],
    [49, "anaflix", "Breaking Bad", "Tarda en arrancar, pero cuando arranca no para. Walter White es increíble.", 5, 143],
    [50, "tomasreview", "Cats", "     ya la bi y sigo sin entender q vi. alguien me la esplica?     ", 0, 0],
]