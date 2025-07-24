class Stack:
    def __init__(self):#sel hace ref a el mimsmo objeto de la clase
        self.__stack_list = []#se hace privado por tener "__"
    def push(self, valor):
        self.__stack_list.append(valor)
    def pop(self):
        valor = self.__stack_list[-1]
        del self.__stack_list[-1]
        return valor

class Agregar_al_stack(Stack):#hereda de Stack
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    def get_sum(self):
        return self.__sum
    
    def push(self, valor):
        self.__sum += valor
        Stack.push(self, valor)
        
    def pop(self):
        valor = Stack.pop(self)
        self.__sum -= valor
        return valor


objeto_stack = Agregar_al_stack()

for i in range(5):
    objeto_stack.push(i)
print(objeto_stack.get_sum())

for i in range(5):
    print(objeto_stack.pop())
    