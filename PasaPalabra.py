import random


def sigue_el_jugo(sigue_jugando):
    if sigue_jugando == "5":
        print("Excelente ! Sigamos jugando")
        entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
        return entrada
    else:
        if sigue_jugando == "9":
            print(
                f"Usted a finalizado el juego \ncantidad de respuestas correctas:{resp_correctas}\ncantidad de respuestas incorrectas:{resp_incorrectas}".upper())
            entrada = "1"
            return entrada


letra = str
# print(string.ascii_uppercase)
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "y", "z"]
# print(f"{abecedario}")
# A CONTINUACION SE DEPOSITAN LAS PREGUNTAS
pregunta_a = "Secuencia de pasos ordenados que describen un proceso"
pregunta_b = "Tipo de dato logico"
pregunta_c = "Número o caracter que se utiliza como un valor y no cambiara al menos dentro de un algoritmo"
pregunta_d = "PRIMERA parte fundamental en la vida de una variable. Este proceso se aconseja hacerlo al inicio del algoritmo"
pregunta_e = "Tipo de dato numero donde no se tienen en cuenta la parte decimal, es catellano"
pregunta_f = "Estado logico consecuencia de no cumplirse una preposición"
pregunta_g = "Contiene \"G\", tipo de operador donde se comparan valores booleanos y el resultado es logico"
pregunta_h = "Contiene \"H\", nombre de uno de los IDE de PYTHON"
pregunta_i = "Estructura selectiva simple, en ingles"
pregunta_j = "Lenguaje de programacion orientado a objetos"
pregunta_k = "Sentencia imterrumpir, se utiliza para terminar un bucle en un lugar determinado. En ingles"
pregunta_l = "Contiene \"L\", Acción de transformar un programa desde lenguaje de programacion a codigo maquina"
pregunta_m = "Contiene \"M\": Software encargado de transformar un lenguaje de alto nivel en codigo maquina"
pregunta_n = "Contiene \"N\": Subprgrama que se define y se puede llamar cada vez que lo necesitemos en el codigo"
pregunta_o = "Contiene \"O\": Parte de todo algoritmo compuesta por el conjunto de instrucciones"
pregunta_p = "Respresentacion escrita de instrucciones, previa a desarrollar el algoritmo"
pregunta_q = "Evolución del codigo de barras. Tambien llamado codigo de barras bidimensional"
pregunta_r = "Tipo de estructura donde un conjunto de instrucciones se repiten un número determinado de veces o hasta cumplirse una condición"
pregunta_s = "Secuancia de dato utilizada para representar texto. En ingles"
pregunta_t = ""
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
entrada = input("Ingrese \"0\" para obtener una letra: ").upper()
resp_correctas = 0
resp_incorrectas = 0
while entrada == "0":
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "y", "z"]
    posicion_letra = random.randrange(0, 1)  # Número aleatorio para sacar una letra de la lista abecedario
    letra = abecedario[posicion_letra]
    if letra == "a":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:\n{pregunta_a}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_a:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)         #SE LLAMA A LA FUNCION QUE VERIFICA SI SIGUE O NO EL JUEGO
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "b":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_b}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_b:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "c":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print("La Pregunta es: ")
        # FALTA PREGUNTA
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == "c":  # FALTA CORREGIR LA CONDICION
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "d":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_d}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_d:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "e":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_e}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_e:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "f":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_f}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_f:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "g":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_g}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_g:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "h":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_h}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_h:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "i":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_i}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_i:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "j":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_j}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_j:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "k":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_k}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_k:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "l":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_l}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_l:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "m":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_m}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_m:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "n":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_n}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_n:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "o":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_o}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_o:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "p":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_p}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_p:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "q":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_q}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_q:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "r":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_r}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_r:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "s":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_s}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_s:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
    if letra == "r":
        print(f"La letra salida al azar es \"{letra}\"".upper())
        print(f"La Pregunta es:{pregunta_r}")
        respuesta = input("Ingrese su respuesta: ").lower()
        if respuesta == respuesta_r:
            resp_correctas = (resp_correctas + 1)
            print("La respuesta es correcta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
        else:
            resp_incorrectas = (resp_incorrectas + 1)
            print("La respuesta es incorrecta".upper())
            sigue_jugando = input("¿Desea continuar jugando?\nIngrese \"5\" para continuar o \"9\" para terminar: ".upper())
            entrada = sigue_el_jugo(sigue_jugando)
