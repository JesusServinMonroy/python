class EjemploClase:
    contador = 0#solo existe una copia de las variables de clase poesasr de que haya varios objetos de clase
    def __init__(self, valor = 1):
        self.primera = valor
        EjemploClase.contador += 1

    def set_segunda(self, valor):
        self.segunda = valor
        
class Ejemplo2:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


objeto1 = EjemploClase()
objeto2 = EjemploClase(2)

objeto2.set_segunda(3)

objeto3 = EjemploClase(4)
objeto3.tercera = 5

print(objeto1.__dict__)#solo tiene la varible primera ; con dict no se muestra varibales de clase 
print(objeto2.__dict__)#tiene la variable primera y segunda
print(objeto3.__dict__)#tiene primera y segunda, y asu ves agrega la varible tercera 

print(objeto1.contador)
print(objeto2.contador)
print(objeto3.contador)

example_object = Ejemplo2(1)
print(example_object.a)
#uso try except para notener un error al llamar a b 
try:
    print(example_object.b)
except AttributeError:
    pass

if hasattr(example_object, 'b'):## hasattr verifica con seguridad si algún objeto / clase contiene una propiedad específica.devuelve un true o false
    print(example_object.b)