from PasaPalabra import juegoPasaPalabra
def menu():
    global opcion,salir
    print('¿Que juego quieres jugar?');
    print('1. BlackJack');
    print('2. Pasapalabra');
    print('3. Preguntados');
    print('4. Salir');
    opcion = input('Elige una opcion: ');
    if opcion == '1':
        from blackJack import comenzarJuego;
        comenzarJuego();
    elif opcion == '2':
            juegoPasaPalabra();
    elif opcion == '3':
        from preguntados import jugar1;
        jugar1();
        print('Preguntados');
    elif opcion == '4':
        print('Hasta luego!');
        exit();
    salir=opcion
    
menu()