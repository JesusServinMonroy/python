def dos_digitos(valor):
    s = str(valor)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer:
    def __init__(self, horas=0, minutos=0, segundos=0):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        return dos_digitos(self.__horas) + ":" + \
                dos_digitos(self.__minutos) + ":" + \
                dos_digitos(self.__segundos)

    def segundo_siguiente(self):
        self.__segundos += 1
        if self.__segundos > 59:
            self.__segundos = 0
            self.__minutos += 1
            if self.__minutos > 59:
                self.__minutos = 0
                self.__horas += 1
                if self.__horas > 23:
                    self.__horas = 0

    def segundo_anterior(self):
        self.__segundos -= 1
        if self.__segundos < 0:
            self.__segundos = 59
            self.__minutos -= 1
            if self.__minutos < 0:
                self.__minutos = 59
                self.__horas -= 1
                if self.__horas < 0:
                    self.__horas = 23


timer = Timer(22, 59, 59)
print(timer)
timer.segundo_siguiente()
print(timer)
timer.segundo_anterior()
print(timer)
    