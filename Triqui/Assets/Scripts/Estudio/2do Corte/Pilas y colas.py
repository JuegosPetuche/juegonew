class Nodo:

    def __init__(self, dato):

        self.dato = dato
        self.siguiente = None

class Pila:

    cabeza = None
    
    def añadir(self, dato):

        nuevoNodo = Nodo(dato)

        if self.cabeza ==  None:
            self.cabeza = nuevoNodo

        else:
            nuevoNodo.siguiente = self.cabeza
            self.cabeza = nuevoNodo

    def sacar(self):
            
        actual = self.cabeza
        self.cabeza = actual.siguiente


    def verPrimero(self):

        print(self.cabeza.dato)

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
            self.cola = nuevoNodo
        
    def quitar(self):

        actual = self.cabeza
        self.cabeza = actual.siguiente
        actual.siguiente = None

    def mostrar(self):

        print(f"Esta es la cabeza: {self.cabeza.dato}")
        print(f"Esta es la cola: {self.cola.dato}")
            
