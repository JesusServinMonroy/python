##implementar la clase Queue con dos operaciones básicas:

#put(elemento), que coloca un elemento al final de la cola.
#get(), que toma un elemento del principio de la cola y lo devuelve como resultado 
# (la cola no puede estar vacía para realizarlo correctamente).
#método sin parámetros que devuelva True si la cola está vacía y False de lo contrario.
class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    
    def put(self, elem):
        self.queue.insert(0, elem)
    
    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

class SuperQueue(Queue):
    def isempty(self):
        return len(self.queue) == 0


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        if not que.isempty():
            print(que.get())
except:
    print("Cola vacía")
