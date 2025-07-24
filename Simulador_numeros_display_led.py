DIGITOS = {
    '0': [
        "###",
        "# #",
        "# #",
        "# #",
        "###"
    ],
    '1': [
        "  #",
        "  #",
        "  #",
        "  #",
        "  #"
    ],
    '2': [
        "###",
        "  #",
        "###",
        "#  ",
        "###"
    ],
    '3': [
        "###",
        "  #",
        "###",
        "  #",
        "###"
    ],
    '4': [
        "# #",
        "# #",
        "###",
        "  #",
        "  #"
    ],
    '5': [
        "###",
        "#  ",
        "###",
        "  #",
        "###"
    ],
    '6': [
        "###",
        "#  ",
        "###",
        "# #",
        "###"
    ],
    '7': [
        "###",
        "  #",
        "  #",
        "  #",
        "  #"
    ],
    '8': [
        "###",
        "# #",
        "###",
        "# #",
        "###"
    ],
    '9': [
        "###",
        "# #",
        "###",
        "  #",
        "###"
    ]
}


def mostrar_display(numero):
    filas = [""] * 5  # 5 elementos-str por digito
    for digito in numero:
        patron = DIGITOS.get(digito, ["   "] * 5)#valor por default por si el valor no existe
        for i in range(5):
            filas[i] += patron[i] + "  "  # Espacio entre dígitos
    for fila in filas:
        print(fila)


numero = input("dame un numero entero no negativo: ")
mostrar_display(numero)