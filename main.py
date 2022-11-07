from blackJack import comenzarJuego;
from pasaPalabra import juegoPasaPalabra;
# menu
def menu():
    print('¿Que juego quieres jugar?');
    print('1. BlackJack');
    print('2. Pasapalabra');
    print('3. Preguntados');
    print('4. Salir');
    opcion = input('Elige una opcion: ');
    
    if opcion == '1':
        comenzarJuego();
    elif opcion == '2':
        juegoPasaPalabra();
    elif opcion == '3':
        print('Preguntados');
    elif opcion == '4':
        print('Hasta luego!');
        exit();
menu();