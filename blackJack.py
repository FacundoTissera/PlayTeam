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


# creo funcion para mostrar las cartas de cada mano del dealer
def manoDealer():

    # si el total de cartas que tiene la casa es igual a 2 que muestre solo la primera carta
    if len(manoCasa) == 2:
        return manoCasa[0];
    
    elif len(manoCasa) > 2:
        return manoCasa[0], manoCasa[1];



# bucle para el juego
for i in range(2):
    repartirCartas(manoCasa);
    repartirCartas(manoJugador);

# print(manoCasa)
# print(manoJugador)

# mientras que jugador sea verdadero entre al bucle
while jugador or dealer:
    print(f'dealer tiene {manoDealer()}  y X');
    print(f' tu tienes {manoJugador} y el total es {totalMano(manoJugador)}')

    # si el total de la mano del jugador es menor a 21 que le pregunte si quiere otra carta
    if jugador:
        plantarseOPedir = input('Quieres otra carta? (y/n) ').lower();
    

    if totalMano(manoCasa) > 16:
        dealer = False;
    else:
        repartirCartas(manoCasa);
    if plantarseOPedir == 'n':
        jugador = False;
    else:
        repartirCartas(manoJugador);
    if totalMano(manoJugador) >= 21:
        break;
    elif totalMano(manoCasa) >= 21:
        break;


# si jugaror tiene 21 que gane
if totalMano(manoJugador) == 21:
    print(f'\n Tu tienes {manoJugador} para un total de {totalMano(manoJugador)} y el Dealer tiene {manoCasa} para un total de {totalMano(manoCasa)} \n')
    print('BlackJack!! --> Tu Ganas!');

# si dealer tiene 21 que gane
elif totalMano(manoCasa) == 21:
    print(f'\n Tu tienes {manoJugador} para un total de {totalMano(manoJugador)} y el Dealer tiene {manoCasa} para un total de {totalMano(manoCasa)} \n')
    print('BlackJack!! --> Dealer Gana!');

# si el total de jugador es mayor a 21 que pierda
elif totalMano(manoJugador) > 21:
    print(f'\n Tu tienes {manoJugador} para un total de {totalMano(manoJugador)} y el Dealer tiene {manoCasa} para un total de {totalMano(manoCasa)} \n')
    print('Tu pierdes, te pasaste de 21 y el Dealer gana!');

# si el total de dealer es mayor a 21 que pierda
elif totalMano(manoCasa) > 21:
    print(f'\n Tu tienes {manoJugador} para un total de {totalMano(manoJugador)} y el Dealer tiene {manoCasa} para un total de {totalMano(manoCasa)} \n')
    print('El Dealer se paso de 21, Tu ganas!');

# si el jugador se planta que reste  la mano del dealer menos 21 y si es menor que la del jugador que gane el dealer porque le falta menos para llegar a 21
elif 21 - totalMano(manoCasa) < 21 - totalMano(manoJugador):
    print(f'\n Tu tienes {manoJugador} para un total de {totalMano(manoJugador)} y el Dealer tiene {manoCasa} para un total de {totalMano(manoCasa)} \n')
    print('Dealer gana!');

# si el jugador se planta que reste  la mano del dealer menos 21 y si es mayor que la del jugador que gane el jugador porque le falta menos para llegar a 21
elif 21 - totalMano(manoCasa) > 21 - totalMano(manoJugador):
    print(f'\n Tu tienes {manoJugador} para un total de {totalMano(manoJugador)} y el Dealer tiene {manoCasa} para un total de {totalMano(manoCasa)} \n')
    print('Tu ganas!');



