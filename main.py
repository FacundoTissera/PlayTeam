def menu():
    
    global opcion, salir
    print('¿Que juego quieres jugar?');
    print('1. BlackJack');
    print('2. Pasapalabra');
    print('3. Preguntados');
    print('4. Piedra, Papel o Tijera');
    print('5. Salir');
    opcion = input('Elige una opcion: ');
    
    if opcion == '1':
        from blackJack import comenzarJuego;
        comenzarJuego();
    
    elif opcion == '2':
        from PasaPalabra import entrada;
        entrada()
    
    elif opcion == '3':
        from preguntados import jugar1;
        jugar1();
        
    elif opcion == '4':
        from piedrapapeltijera import piedraPapelTijera;
        piedraPapelTijera();
    
    elif opcion == '5':
        print('Hasta luego!');
        exit();
    
    salir = opcion


menu()
