"""Datos iniciales del sistema de reseñas de películas y series."""
 
# Posición de cada columna dentro de un registro
ID = 0
USUARIO = 1
TITULO = 2
PUNTUACION = 3
LIKES = 4
TEXTO = 5

# Rango de puntuaciones de las reseñas 
PUNTUACION_MIN = 0
PUNTUACION_MAX = 5

resenias = [
    [1, "cinefilo92", "El Padrino", 5, 342, "Una obra maestra del cine. La actuación de Marlon Brando es inolvidable y la música acompaña cada escena."],
    [2, "lauramovies", "Toy Story 3", 5, 128, "   Me hizo llorar como a una nena. Pixar sabe tocar el corazón de grandes y chicos.   "],
    [3, "popcorn88", "Breaking Bad", 5, 512, "LA MEJOR SERIE DE LA HISTORIA. NO HAY DISCUSIÓN."],
    [4, "nachocritico", "Avatar: El camino del agua", 3, 87, "Visualmente impresionante, pero el guion es flojo. Mucho efecto y poca historia, mucho ruido y pocas nueces."],
    [5, "seriefan", "Stranger Things", 4, 64, "Spoiler: Eleven vuelve a salvar a todos. La temporada es buena, pero el spoiler del final me lo arruinaron en redes."],
    [6, "martintv", "Relatos salvajes", 5, 203, "Humor negro argentino en su máxima expresión. Cada relato es mejor que el anterior."],
    [7, "sofi2000", "Cats", 1, 15, "    no la recomiendo. aburrida,  rara  y larga. muy, muy larga. q alguien me debuelva las 2 horas    "],
    [8, "GuilleCine", "El secreto de sus ojos", 5, 276, "Ricardo Darín está brillante. La escena del estadio es una de las mejores del cine argentino."],
    [9, "anaflix", "The Office", 4, 98, "  divertida, incómoda y entrañable. michael scott es un personaje único.  "],
    [10, "tomasreview", "Joker", 4, 154, "Una actuación enorme de Joaquin Phoenix. La película es oscura, oscura de verdad, y no es para todos."],
    [11, "cinefilo92", "Interestelar", 5, 301, "Ciencia y emoción en partes iguales. La banda sonora de Hans Zimmer es épica."],
    [12, "lauramovies", "Emily en París", 3, 22, "linda para pasar el rato aunque los cliches sobre francia cansan un poco... ay capitulos q son iguales"],
    [13, "popcorn88", "Game of Thrones", 2, 445, "Siete temporadas geniales y una octava para el olvido. Spoiler: el final decepciona."],
    [14, "nachocritico", "Oppenheimer", 4, 190, "Larga pero atrapante. Nolan vuelve a jugar con el tiempo y la narrativa."],
    [15, "seriefan", "Dark", 5, 167, "¿Quién es quién? ¿Cuándo pasa qué? Hay que verla con un cuaderno al lado, pero vale la pena."],
    [16, "martintv", "Los Simuladores", 5, 133, "   CLÁSICO de la televisión argentina. Santos, Medina, Lamponne y Ravenna son inolvidables.   "],
    [17, "sofi2000", "Titanic", 4, 58, "  Romantica y trajica. La bi diez veces y la beria diez veces mas!!!  "],
    [18, "GuilleCine", "Nueve reinas", 5, 141, "Un guion perfecto. Nunca sabés quién engaña a quién hasta el final."],
    [19, "anaflix", "Black Mirror", 4, 76, "Algunos capítulos son geniales y otros no tanto. La tecnología como espejo de lo peor de nosotros."],
    [20, "tomasreview", "Batman v Superman", 2, 9, "   mucho ruido poca historia xq ni batman ni superman se salvan de un guion confuso   "],
    [21, "cinefilo92", "Ciudad de Dios", 5, 188, "Cruda y real. Una película necesaria que no se olvida fácilmente."],
    [22, "lauramovies", "Frozen", 3, 0, "  La canción es pegadiza, demasiado pegadiza. Mis sobrinos no paran de cantarla.  "],
    [23, "popcorn88", "The Mandalorian", 4, 230, "Baby Yoda se roba cada escena. Spoiler: aparece Luke en el final de la segunda temporada."],
    [24, "nachocritico", "Tenet", 3, 112, "No entendí nada. Volví a verla y entendí un poco menos. Igual la recomiendo."],
    [25, "seriefan", "La casa de papel", 3, 45, "  las primeras partes son muy buenas, despues se estira demaciado. aver si la ultima temporada lo arregla  "],
    [26, "martintv", "Okupas", 5, 97, "Una joya del 2000. Realismo puro y personajes que se sienten reales."],
    [27, "sofi2000", "Crepúsculo", 0, 3, "mala. mala. mala. no tengo más para decir."],
    [28, "GuilleCine", "Argentina, 1985", 5, 389, "Una película importante y emocionante. La actuación de Darín y Lanzani es excelente."],
    [29, "anaflix", "Friends", 5, 61, "  NUNCA ME CANSO DE VERLA. ES MI SERIE DE CONFORT.  "],
    [30, "tomasreview", "Morbius", 1, 4, "ni el elenco la salva.   aburrida de principio a fin, no se q estaban pensando"],
    [31, "cinefilo92", "Parásitos", 5, 254, "Una crítica social brillante disfrazada de thriller. Merecido el Oscar."],
    [32, "lauramovies", "Bridgerton", 3, 18, "    Bestuario ermoso y mucho drama. Ideal para un domingo de lluvia    "],
    [33, "popcorn88", "The Last of Us", 5, 377, "Spoiler: el tercer capítulo es el mejor de la serie. Bill y Frank son inolvidables."],
    [34, "nachocritico", "Barbie", 4, 143, "Más inteligente de lo que esperaba. Divertida y con un mensaje claro."],
    [35, "seriefan", "Merlina", 4, 89, "La actuación de Jenna Ortega sostiene toda la serie. El baile ya es un clásico."],
    [36, "martintv", "Esperando la carroza", 5, 214, "¡Tres empanadas! Un clásico que se ve una y otra vez y siempre da risa."],
    [37, "sofi2000", "Diario de una pasión", 4, 37, "  llore, llore y llore... MUY RECOMENDABLE para ver con pañuelos  "],
    [38, "GuilleCine", "El clan", 4, 122, "Perturbadora y bien filmada. Guillermo Francella sorprende en un papel oscuro."],
    [39, "anaflix", "Sex Education", 4, 0, "Fresca, honesta y divertida. Los personajes crecen temporada a temporada."],
    [40, "tomasreview", "Rápidos y furiosos 9", 1, 31, "AUTOS EN EL ESPACIO. si, autos en el espacio. no ay mas preguntas"],
    [41, "cinefilo92", "Pulp Fiction", 5, 289, "Diálogos inolvidables y una estructura que rompe todas las reglas."],
    [42, "lauramovies", "Mamma Mia", 4, 27, "musica de abba, paisajes griegos y buena energia. imposible no cantar!!"],
    [43, "popcorn88", "Succession", 5, 198, "Personajes horribles que no podés dejar de mirar. Spoiler: nadie gana."],
    [44, "nachocritico", "Dune", 4, 156, "Épica, lenta y visualmente perfecta. Hay que verla en el cine."],
    [45, "seriefan", "Euphoria", 3, 52, "   Estética increíble pero la historia a veces se pierde.   "],
    [46, "martintv", "Casados con hijos", 4, 79, "Pepe Argento es un personaje eterno. La repiten y la vuelvo a ver."],
    [47, "sofi2000", "Sharknado", 1, 12, "  tan mala q es buena. o no. definitivamente no. NO LA BEAN  "],
    [48, "GuilleCine", "Relatos salvajes", 5, 167, "El episodio de la boda es mi favorito. Erica Rivas está espectacular."],
    [49, "anaflix", "Breaking Bad", 5, 143, "Tarda en arrancar, pero cuando arranca no para. Walter White es increíble."],
    [50, "tomasreview", "Cats", 0, 0, "     ya la bi y sigo sin entender q vi. alguien me la esplica?     "],
]