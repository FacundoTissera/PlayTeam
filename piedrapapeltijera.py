# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).

import random
jugada = 0
cant_ganadas = 0
cant_perdidas = 0
while jugada < 3:
		jugada = jugada + 1
		jugada_usuario = int(input("Elija su jugada: 1.- Piedra, 2.- Papel, 3.- Tijera: "))
		while jugada_usuario > 3 or jugada_usuario < 1:
			jugada_usuario = int(input("Elija su jugada: 1.- Piedra, 2.- Papel, 3.- Tijera: "))
			# jugada_usuario = jugada_usuario
		if jugada_usuario==1:
			print("Ustes elijio: Piedra")
		if jugada_usuario==2:
			print("Usted eligio: Papel")
		if jugada_usuario==3:
			print("Usted eligio: Tijera")
		if jugada_usuario<1 or jugada_usuario>3:
			print("El valor es incorrecto. Ingresalo nuevamente")

		jugada_ordenador = random.randrange(1,4)
		if jugada_ordenador==1:
			print("Jugada ordenador: Piedra")
		if jugada_ordenador==2:
			print("Jugada ordenador: Papel")
		if jugada_ordenador==3:
			print("Jugada ordenador: Tijera")

		if jugada_usuario == jugada_ordenador:
			while jugada_usuario == jugada_ordenador:
				print("Empate: La partida se vuelve a jugar!")
				jugada_usuario = int(input("Elija su jugada: 1.- Piedra, 2.- Papel, 3.- Tijera."))
				if jugada_usuario == 1:
					print("Piedra")
				if jugada_usuario == 2:
					print("Papel")
				if jugada_usuario == 3:
					print("Tijera")
				if jugada_usuario < 1 or jugada_usuario > 3:
					print("El valor es incorrecto. Ingresalo nuevamente")

				jugada_ordenador = random.randrange(1, 4)
				if jugada_ordenador == 1:
					print("Jugada ordenador: Piedra")
				if jugada_ordenador == 2:
					print("Jugada ordenador: Papel")
				if jugada_ordenador == 3:
					print("Jugada ordenador: Tijera")

		if (jugada_usuario==1 and jugada_ordenador==3) or (jugada_usuario==2 and jugada_ordenador==1) or (jugada_usuario==3 and jugada_ordenador==2):
			print("Gana usuario")
			cant_ganadas = cant_ganadas+1

		if (jugada_usuario==3 and jugada_ordenador==1) or (jugada_usuario==1 and jugada_ordenador==2) or (jugada_usuario==2 and jugada_ordenador==3):
			print("Gana ordenador")
			cant_perdidas = cant_perdidas+1

if jugada==3:
	if cant_ganadas>cant_perdidas:
		print(f"Usted a ganado el juego con ",{cant_ganadas}," partidas ganadas")
	if cant_perdidas>cant_ganadas:
		print(f"Usted a perdido el juego, el ordenador a ganado ",{cant_perdidas}," partidas")

