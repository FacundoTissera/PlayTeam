import random

# Esta funcion verifica que el usuario ingrese solo 5 o 9 para seguir o no jugando
def verificar5o9(sigue_jugando):
    while sigue_jugando != "5" and sigue_jugando != "9":
        sigue_jugando = input(
            "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
        sigue_jugando = sigue_jugando
    return sigue_jugando

# Esta funcion asegura que sea 0 lo que ingresa el usuario para pedir una nueva letra
def verificarentrada(entrada):
    while entrada != "0":
        entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
        entrada = entrada
    return entrada

# Esta funcion comprueba si se ingreso 5 o 9 para terminar el juego o no
def sigue_el_jugo(sigue_jugando):
        if sigue_jugando == "5":
            print("Excelente ! Sigamos jugando")
            entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
            entrada = verificarentrada(entrada)
            return entrada
        elif sigue_jugando == "9":
            print(f"Usted a finalizado el juego !! \nLa cantidad de respuestas correctas:{resp_correctas}\nLa cantidad de respuestas incorrectas:{resp_incorrectas}".upper())
            entrada = "1"
            return entrada



# A CONTINUACION SE DEPOSITAN LAS PREGUNTAS
pregunta_a = "Secuencia de pasos ordenados que describen un proceso"
pregunta_b = "Tipo de dato logico"
pregunta_c = "Número o caracter que se utiliza como un valor y no cambiara al menos dentro de un algoritmo"
pregunta_d = "PRIMERA parte fundamental en la vida de una variable. Este proceso se aconseja hacerlo al inicio del algoritmo"
pregunta_e = "Tipo de dato numerico donde no se tienen en cuenta la parte decimal, es catellano"
pregunta_f = "Estado logico consecuencia de no cumplirse una preposición. En castellano"
pregunta_g = "Contiene \"G\": tipo de operador donde se comparan valores booleanos y el resultado es logico"
pregunta_h = "Contiene \"H\": nombre de uno de los IDE de PYTHON"
pregunta_i = "Estructura selectiva simple, en ingles"
pregunta_j = "Lenguaje de programacion orientado a objetos"
pregunta_k = "Sentencia imterrumpir, se utiliza para terminar un bucle en un lugar determinado. En ingles"
pregunta_l = "Contiene \"L\": Acción de transformar un programa desde lenguaje de programacion a codigo maquina"
pregunta_m = "Contiene \"M\": Software encargado de transformar un lenguaje de alto nivel en codigo maquina"
pregunta_n = "Contiene \"N\": Subprograma que se define y se puede llamar cada vez que lo necesitemos en el codigo"
pregunta_o = "Contiene \"O\": Parte de todo algoritmo compuesta por el conjunto de instrucciones"
pregunta_p = "Respresentacion escrita de instrucciones, previa a desarrollar el algoritmo"
pregunta_q = "Evolución del codigo de barras. Tambien llamado codigo de barras bidimensional"
pregunta_r = "Tipo de estructura donde un conjunto de instrucciones se repiten un número determinado de veces o hasta cumplirse una condición"
pregunta_s = "Tipo de dato utilizada para almacenar y manipular texto. En ingles"
pregunta_t = "Contiene \"T\": Tipo de dato alphanumerico. En castellano"
pregunta_u = "Contine \"U\": Denominacion que se le otorga a una fraccion de una cadena de caracteres"
pregunta_v = "Espacio de memoria donde se alamacen datos que pueden modificarse durante el codigo"
pregunta_w = "Estructura repetitiva donde la condicion se analiza antes de ingresar al bucle. En ingles"
pregunta_y = "Contiene \"Y\": Conjunto de 8 bits"
pregunta_z = "Extensión de archivos comprimidos"

# A CONTINUACION SE DEPOSITAN LAS RESPUESTAS
respuesta_a = "algoritmo".lower()
respuesta_b = "booleano".lower()
respuesta_c = "constante".lower()
respuesta_d = "declaracion".lower()
respuesta_e = "entero".lower()
respuesta_f = "falso".lower()
respuesta_g = "logico".lower()
respuesta_h = "pycharm".lower()
respuesta_i = "if".lower()
respuesta_j = "java".lower()
respuesta_k = "break".lower()
respuesta_l = "compilar".lower()
respuesta_m = "compilador".lower()
respuesta_n = "funcion".lower()
respuesta_o = "proceso".lower()
respuesta_p = "pseudocodigo".lower()
respuesta_q = "qr".lower()
respuesta_r = "repetitiva".lower()
respuesta_s = "string".lower()
respuesta_t = "caracter".lower()
respuesta_u = "subcadena".lower()
respuesta_v = "variable".lower()
respuesta_w = "while".lower()
respuesta_y = "byte".lower()
respuesta_z = "zip".lower()

# Se declara el abecedario que se va a usar, variables y arrays.
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
              "u", "v", "w", "y", "z"]
letra = str
letras_ya_salidas = []
resp_correctas = int
resp_incorrectas = int

# Comienza el juego, se verifica que sea 0 lo que ingreso el usuario y se inicializan los contadores en 0(cero).
entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
entrada = verificarentrada(entrada)
resp_correctas = 0
resp_incorrectas = 0

# Este condicional verifica que el usuario quiso comenzar el juego o lo abandono.
while entrada == "0":

    # Comprobamos que el usuario haya recorrido todas las letras
    if len(abecedario) == len(letras_ya_salidas):
        print(f"Usted a recorrido todo el juego y sus resultados son: \nRespuestas Correctas:{resp_correctas}//25"
              f"\nRespuestas Incorrectas:{resp_incorrectas}//25")
        break

    # Obtenemos un numero aleatorio para ir a buscar una letra en esa posicion dentro del abecedario
    posicion_letra = random.randrange(0, 25)

    # Buscamos la letra en el arrays abecedario que corresponde con ese valor de posición
    letra = abecedario[posicion_letra]

    # Se verifica que la letra obtenida al azar haya salido  o no anteriormente, de ser asi se vuelve a buscar otra letra
    while letra in letras_ya_salidas:
        posicion_letra = random.randrange(0, 25)
        letra = abecedario[posicion_letra]

    # Se almacena la letra que se utilizo en un nuevo arrays que se utiliza para verificar si la letra se uso ya o no
    letras_ya_salidas.append(letra)

    # print(letras_ya_salidas)

    # Cada if verifica la coincidencia por cada letra para imprimir la pregunta y verificar si es correcta o no la respuesta
    if letra == "a":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_a}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_a:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)    # Se verifica que sea efectivamente 5 o 9
            entrada = sigue_el_jugo(sigue_jugando)  # SE LLAMA A LA FUNCION QUE VERIFICA SI SIGUE O NO EL JUEGO
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "b":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_b}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_b:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "c":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_c}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_c:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "d":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_d}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_d:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "e":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_e}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_e:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "f":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_f}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_f:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "g":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_g}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_g:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "h":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_h}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_h:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "i":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_i}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_i:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "j":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_j}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_j:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "k":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_k}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_k:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "l":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_l}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_l:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "m":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_m}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_m:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "n":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_n}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_n:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "o":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_o}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_o:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "p":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_p}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_p:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "q":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_q}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_q:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "r":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_r}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_r:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "s":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_s}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_s:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "t":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_t}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_t:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "u":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_u}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_u:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "v":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_v}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_v:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "z":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es: {pregunta_z}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_z:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input(
                "¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            sigue_jugando = verificar5o9(sigue_jugando)
            entrada = sigue_el_jugo(sigue_jugando)
