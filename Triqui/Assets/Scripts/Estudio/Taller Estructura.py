class NodoPila:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None
        self.tamaño = 0

    def push(self, dato):
        nuevo = NodoPila(dato)
        nuevo.siguiente = self.tope
        self.tope = nuevo
        self.tamaño += 1

    def pop(self):
        if self.is_empty():
            return None
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        self.tamaño -= 1
        return dato

    def peek(self):
        return self.tope.dato if not self.is_empty() else None

    def is_empty(self):
        return self.tope is None

    def size(self):
        return self.tamaño

    def __str__(self):
        actual = self.tope
        elementos = ""
        while actual:
            elementos += f"{actual.dato} -> "
            actual = actual.siguiente
        return elementos + "None"

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamaño = 0

    def enqueue(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.final:
            self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo
        if not self.frente:
            self.frente = nuevo_nodo
        self.tamaño += 1

    def dequeue(self):
        if self.is_empty():
            return None
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if not self.frente:
            self.final = None
        self.tamaño -= 1
        return dato

    def peek(self):
        return self.frente.dato if not self.is_empty() else None

    def is_empty(self):
        return self.tamaño == 0

    def __str__(self):
        actual = self.frente
        texto = ""
        while actual:
            texto += f"{actual.dato} -> "
            actual = actual.siguiente
        return texto + "None"

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.inicio = None
        self.final = None

    def agregar_final(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if not self.final:
            self.inicio = self.final = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.final
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def recorrer_inicio_fin(self):
        actual = self.inicio
        texto = ""
        while actual:
            texto += f"{actual.dato} <-> "
            actual = actual.siguiente
        return texto + "None"

    def recorrer_fin_inicio(self):
        actual = self.final
        texto = ""
        while actual:
            texto += f"{actual.dato} <-> "
            actual = actual.anterior
        return texto + "None"

    def __str__(self):
        return f"\nInicio a Fin: {self.recorrer_inicio_fin()}\nFin a Inicio: {self.recorrer_fin_inicio()}"

class Hospital:
    def __init__(self):
        self.critical_queue = Cola()
        self.severe_queue = Cola()
        self.mild_queue = Cola()
        self.quick_review_queue = Cola()
        self.historial = ListaDoblementeEnlazada()

    def registrar_paciente(self, nombre, edad, nivel_urgencia):
        paciente = {"nombre": nombre, "edad": edad, "nivel_urgencia": nivel_urgencia}
        if nivel_urgencia == 1:
            self.critical_queue.enqueue(paciente)
        elif nivel_urgencia == 2:
            self.severe_queue.enqueue(paciente)
        elif nivel_urgencia == 3:
            self.mild_queue.enqueue(paciente)
            self.quick_review_queue.enqueue(paciente)
        print(f"Paciente {nombre} registrado con urgencia {nivel_urgencia}.")

    def atender_paciente(self):
        if not self.critical_queue.is_empty():
            paciente = self.critical_queue.dequeue()
        elif not self.severe_queue.is_empty():
            paciente = self.severe_queue.dequeue()
        elif not self.mild_queue.is_empty():
            paciente = self.mild_queue.dequeue()
        else:
            print("No hay pacientes en espera.")
            return

        self.historial.agregar_final(paciente)
        print(f"Paciente {paciente['nombre']} atendido.")

    def visualizar_historial(self):
        print(self.historial)

    def activar_revision_rapida(self):
        if self.critical_queue.is_empty() and self.severe_queue.is_empty():
            while not self.quick_review_queue.is_empty():
                paciente = self.quick_review_queue.dequeue()
                print(f"Paciente leve {paciente['nombre']} atendido en revisión rápida.")
        else:
            print("No se puede activar la revisión rápida. Hay pacientes graves o críticos en espera.")

    def menu(self):
        while True:
            print("\n--- Menú Hospital ---")
            print("1. Registrar Paciente")
            print("2. Atender Paciente")
            print("3. Visualizar Historial")
            print("4. Activar Revisión Rápida")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                urgencia = int(input("Nivel de Urgencia (1: crítica, 2: grave, 3: leve): "))
                self.registrar_paciente(nombre, edad, urgencia)
            elif opcion == "2":
                self.atender_paciente()
            elif opcion == "3":
                self.visualizar_historial()
            elif opcion == "4":
                self.activar_revision_rapida()
            elif opcion == "5":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida, intente nuevamente.")

hospital = Hospital()
hospital.menu()
