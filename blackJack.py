import random;

# creo las variables globales para que mientras esto sea tru entre en el while
jugador = True;
dealer = True;

maso = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"];

manoJugador = [];
manoCasa = [];

# creo funcion para repartir cartas a jugador y casa
def repartirCartas(turno):
    # selecciono una carta aleatoria del maso
    carta = random.choice(maso);
    # la agrego a la mano del turno
    turno.append(carta);
    # elimino la carta del maso para que no vuelva a salir
    maso.remove(carta);


# funcion par calcular el total de cada mano y le paso el turno como parametro
def totalMano(turno):
    total = 0;
    valoresDeLetras = [ "J", "Q", "K" ];

#  digo que recorra las cartas por turno
    for carta in turno:
        # si la carta es un numero la suma al total
        if carta in range(1,11):
            total += carta;

        # aca digo que si tca una de estas su valor es 10 y lo sume a totoñ
        elif carta in valoresDeLetras:
            total += 10;

        # aca que cuando toca el A se fije si el total es Mayor a 11 y si es asi que lo sume como 1 sino que su valor sea 11
        else:
            if total > 11:
                total += 1;
            else:
                total += 11;
# devuelvo el total 
    return total;