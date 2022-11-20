import os  # Para limpiar la consola se complementa con el metodo de la linea40 
import random  # Es una libreria Para dar la sensación de aleatoriedad
import urllib.request #ES UN MODULO DE PYTHON PARA ACCEDER USAR RECURSOS DE INTERNET POR URL


def jugar1():
    

 textoBaseDePreguntas = ''''''
filas = [] 
try:
    urlBD = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQFJzqYgyM-Ra-eWlnJ_74Y8oflnB6ARwStAi4gkXnbj9thKQOs5iVTrKk-u9gBY3TE_jGnF6XqQDo0/pub?output=tsv"
    HTTP_response=urllib.request.urlopen(urlBD)
    for line in HTTP_response:#ESTRAEMOS LOS RENGLONES DE NUESTRA BASE DE DATOS EXPORTADA
        filas.append(line.decode("utf-8").replace("\n","").replace("\r",""))#PARA NO AGREGAR LOS RENGLONES VACIOS//UTF-8 es un formato de codificación de caracteres Unicode  Es el responsable de que tu navegador 
                                                                              #te muestre el contenido del texto correctamente decodificado, sin errores ni caracteres extraños.
                                                                              #LINE.DECODE es para decodificar cadenas
except:
    print("No hay conexión a internet, no se pudo cargar la BD")
    exit()
n_pregunta = 0 #es la pregunta que esta contestando el usuario

base_preg = []              #convertimos en un arreglo, donde se representan los datos en una matriz
cantidad = len(filas)     # la cantidad de preguntas es igual a la longuitud de los renglones de excel)

eleccion = [] #arreglos vacios
opciones = []
pregunta = "" #se declara como una varia local con texto vacio y se muestra al imprimir
respuesta = "" #se declara como variable local vacia
puntos=0
incorrectas=0
for i in range(cantidad): #armamos el for para recorrer la cantidad de preguntas, que es igual a las filas del excel)
    if(filas[i] == ""): #la cantidad de filas la obteni de linea 24)
            continue                                         
    base_preg.append(filas[i].split("\t")) ##
    
    
    def borrarConsola():
        os.system("cls" if os.name == "nt" else "clear") #va limpiando la consola esta funcion "CLs" os. system es algo que le digo al sistema operativo, en windows usa la funcion clear)
        
    def elegirpregunta(n):##
        global opciones, respuesta, pregunta ##
        eleccion = base_preg[n] #escogemos la pregunta n alojada en la base de preguntas
        pregunta = eleccion[0]   #el indice 0 en el excel siempre es la pregunta
        respuesta = eleccion[1] #en el uno siempre esta la respuesta correcta-SIEMPRE,se guardo alli a proposito
        opciones = eleccion[1:] #las opciones son las que estan desde el indice 1 hasta el final. los dos puntos: hace que vaya hasta el final)
        for i in range(4): # como la respuesta correcta siempre esta primera, desorganizamos las respuesta con random, con el for disminuye las posibilidades,recorre 4 opciones
          random.shuffle(opciones)#randomizar todos los items de las opciones
        print(opciones)
        return eleccion


    def mostrarPregunta(): #metodo para mostrar la pregunta
        borrarConsola() #borramos la consola
        print()#salto de linea
        print(pregunta) 
        print("A)", opciones[0])
        print("B)", opciones[1])
        print("C)", opciones[2])
        print("D)", opciones[3])
        print()
    def capturarRespuesta(): #capturamos repuesta
        respuestaElegida = ""
        opcionesVálidas = ["a", "b", "c", "d"] #para hacer el if
        while True:#ciclo indefinidopor si elige alguna opcion que no sea ni a b c o D
            respuestaElegida= input("ingrese su respuesta > ").lower() #transforma la respuesta en minuscula
            if not (respuestaElegida in opcionesVálidas):
                print("La respuesta no está entre las opciones válidas, vuelva a intentarlo")
                continue
            break #para que no sea infinito
        return opcionesVálidas.index(respuestaElegida) #que obtenga el index de la repuesta del usuario
    
    def jugar():
        global incorrectas
        elegirpregunta(n_pregunta) #es el numero de pregunta que el usuario esta copntestando
        mostrarPregunta()
        if(n_pregunta==10 or n_pregunta==20 or n_pregunta==30 or n_pregunta==40):    #se agrega este if para ir detectando cuando pasa de una categoria a otra, el avance de categoria
             print("ESTA INICIANDO UN NUEVO NIVEL, FELICITACIONES")                    #el avance significa pasar a otra tematica de preguntas 
             input("ENTER PARA RESPONDER SU NUEVO CICLO DE PREGUNTAS")
        if(opciones[capturarRespuesta()]==respuesta):#capturar respuesta es la que capturamos en la linea 68 y la compara con la repuesta correcta determinada en la linea 45"
              print("Su respuesta es correcta")
              input("ENTER PARA CONTINUAR")
        else:
              print("Su respuesta NO es correcta, la correcta es: "+ respuesta)
              input("ENTER PARA CONTINUAR")
              incorrectas=incorrectas+1
              
              
              
    
    while True:
        try:
            jugar()
        except:
         pass
        n_pregunta += 1
        if(n_pregunta==50 or incorrectas==3):
            borrarConsola()
            print("El juego ha finalizado")
            input("ENTER PARA CONTINUAR")
        break
    
    
