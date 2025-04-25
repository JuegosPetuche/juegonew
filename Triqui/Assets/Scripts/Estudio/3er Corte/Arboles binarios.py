## Son arboles de orden 2
# Ninguno de los nodos debe sobrepasar el grado 2, (osea tener <= 2 hijos)

class Nodo:
    
    def __init__(self, dato):
        self.dato = dato
        self.hijo1 = None
        self.hijo2 = None

class Arbol:

    raiz = None

    def agregar(self, dato):

        nuevoNodo = Nodo(dato)
        if self.raiz == None:

            self.raiz = nuevoNodo

        else:

            self.raiz.hijo1 = nuevoNodo

    def verArbol(self):

        actual = self.raiz
        while actual.hijo1 != None:

            print(f"La raiz es {actual.dato} y su hijo es {actual.hijo1.dato}")
            actual = actual.hijo1

arbol = Arbol()

arbol.agregar(5)
arbol.agregar(3)
arbol.verArbol()