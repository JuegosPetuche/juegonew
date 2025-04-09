class Nodo:

    def __init__(self, dato):

        self.dato = dato
        self.siguiente = None
        self.anterior = None


class Cola:

    cabeza = None
    cola = None

    def agregar(self, dato):

        nuevoNodo = Nodo(dato)

        if self.cabeza == None:

            self.cabeza = nuevoNodo
            self.cola = nuevoNodo

        else:

            self.cola.siguiente = nuevoNodo
            nuevoNodo.anterior = self.cola
            self.cola = nuevoNodo
        
    def quitar(self):

        actual = self.cabeza
        self.cabeza = actual.siguiente
        actual.siguiente = None

    def mostrar(self):

        print(f"Esta es la cabeza: {self.cabeza.dato}")
        print(f"Esta es la cola: {self.cola.dato}")