import os
from random import randrange


def tablero_gato(gato):
	print("+-------" * 3,"+", sep="")
	for fila in range(3):
		print("|       " * 3,"|", sep="")
		for columna in range(3):
			print("|   " + str(gato[fila][columna]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def movimiento_usuario(gato):
	ok = False	# suposición falsa - la necesitamos para entrar en el bucle
	while not ok:
		movimiento = input("Ingresa tu movimiento: ") 
		ok = len(movimiento) == 1 and movimiento >= "1" and movimiento <= "9" # ¿es valido lo que ingreso el usuario?
		if not ok:
			print("Movimiento erróneo, ingrésalo nuevacomputadorante") 
			continue
		movimiento = int(movimiento) - 1 	# mov ucomputadora del 0 al 8
		fila = movimiento // 3 	# fila de la celda
		columna = movimiento % 3		# columnaumna de la celda
		simbolo = gato[fila][columna]
		ok = simbolo not in ["O","X"] 
		if not ok:	# esta ocupado, ingresa una posición nuevacomputadorante
			print("¡Cuadro ocupado, ingresa nuevacomputadorante!")
			continue
	gato[fila][columna] = "O" 	# columnaocar "0" al cuadro seleccionado


def matriz_espacios_gato(gato):
	espacio = []
	for fila in range(3):
		for columna in range(3): 
			if gato[fila][columna] not in ["O","X"]: 
				espacio.append((fila,columna))
	return espacio


def ganador(gato,simbolo):
	if simbolo == "X":	
		quien = "computadora"	
	elif simbolo == "O": 
		quien = "humano"
	else:
		quien = None
	diagonal_1 = diagonal_2 = True  # para las diagonales
	for i in range(3):
		if gato[i][0] == simbolo and gato[i][1] == simbolo and gato[i][2] == simbolo:	# fila i
			return quien
		if gato[0][i] == simbolo and gato[1][i] == simbolo and gato[2][i] == simbolo: # columnaumn i
			return quien
		if gato[i][i] != simbolo: #  diagonal 1
			diagonal_1 = False
		if gato[2 - i][2 - i] != simbolo: # diagonal 2
			diagonal_2 = False
	if diagonal_1 or diagonal_2:
		return quien
	return None


def movimiento_maquina(gato):
	espacio = matriz_espacios_gato(gato) # crea una lista de los cuadros vacios o espacios
	disponible = len(espacio)
	if disponible > 0:	# si la lista no esta vacía, elegir un lugar para "X" y columnaocarla
		seleccion = randrange(disponible)
		fila, columna = espacio[seleccion]
		gato[fila][columna] = "X"


gato = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # matriz 3 x 3
gato[1][1] = "X" # columnaocar la pricomputadorar "X" en el centro
espacio = matriz_espacios_gato(gato)
usuario = True # ¿De quien es turno ahora?
while len(espacio):
	tablero_gato(gato)
	if usuario:
		movimiento_usuario(gato)
		victoria = ganador(gato,"O")
	else:	
		movimiento_maquina(gato)
		victoria = ganador(gato,"X")
	if victoria != None:
		break
	usuario = not usuario		
	espacio = matriz_espacios_gato(gato)
	os.system('cls' if os.name == 'nt' else 'clear')

tablero_gato(gato)
if victoria == "humano":
	print("¡Has ganado!")
elif victoria == "computadora":
	print("¡He ganado!")
else:
	print("¡Empate!")
