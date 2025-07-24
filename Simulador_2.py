digitos = [ #7 segmentos del display led
        '1111110',  # 0
        '0110000',	# 1
        '1101101',	# 2
        '1111001',	# 3
        '0110011',	# 4
        '1011011',	# 5
        '1011111',	# 6
        '1110000',	# 7
        '1111111',	# 8
        '1111011',	# 9
        ]


def imprimir_numero(num):
	global digitos
	digitos_txt = str(num)
	filas = [ '' for lin in range(5) ]
	for d in digitos_txt:
		segmento = [ [' ',' ',' '] for lin in range(5) ]
		patron = digitos[ord(d) - ord('0')]
		if patron[0] == '1':
			segmento[0][0] = segmento[0][1] = segmento[0][2] = '#'
		if patron[1] == '1':
			segmento[0][2] = segmento[1][2] = segmento[2][2] = '#'
		if patron[2] == '1':
			segmento[2][2] = segmento[3][2] = segmento[4][2] = '#'
		if patron[3] == '1':
			segmento[4][0] = segmento[4][1] = segmento[4][2] = '#'
		if patron[4] == '1':
			segmento[2][0] = segmento[3][0] = segmento[4][0] = '#'
		if patron[5] == '1':
			segmento[0][0] = segmento[1][0] = segmento[2][0] = '#'
		if patron[6] == '1':
			segmento[2][0] = segmento[2][1] = segmento[2][2] = '#'
		for lin in range(5):
			filas[lin] += ''.join(segmento[lin]) + ' '
	for lin in filas:
		print(lin)


imprimir_numero(int(input("Ingresa el número que deseas mostrar: ")))