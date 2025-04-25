
class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        if not self.is_empty():
            return self.elementos.pop()
        return None  # Si la pila está vacía

    def peek(self):
        if not self.is_empty():
            return self.elementos[-1]
        return None

    def is_empty(self):
        return len(self.elementos) == 0

    def size(self):
        return len(self.elementos)

    def __str__(self):
        return str(self.elementos)


#### Estructura: Cola

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
        if not self.is_empty():
            dato = self.frente.dato
            self.frente = self.frente.siguiente
            if not self.frente:  # Si la cola queda vacía
                self.final = None
            self.tamaño -= 1
            return dato
        return None

    def peek(self):
        if not self.is_empty():
            return self.frente.dato
        return None

    def is_empty(self):
        return self.tamaño == 0

    def __str__(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return str(elementos)


#### Estructura: Lista Doblemente Enlazada
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
        if not self.final:  # Si la lista está vacía
            self.inicio = self.final = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.final
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def recorrer_inicio_fin(self):
        actual = self.inicio
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

    def recorrer_fin_inicio(self):
        actual = self.final
        elementos = []
        while actual:
            elementos.append(actual.dato)
            actual = actual.anterior
        return elementos

    def __str__(self):
        return f"Inicio a Fin: {self.recorrer_inicio_fin()} | Fin a Inicio: {self.recorrer_fin_inicio()}"

class Hospital:
    def __init__(self):
        self.critical_queue = Cola()
        self.severe_queue = Cola()
        self.mild_queue = Cola()
        self.quick_review_queue = Cola()
        self.historial = ListaDoblementeEnlazada()
        self.medicamentos_pacientes = {}  # Diccionario {'nombre_paciente': Pila}

    def registrar_paciente(self, nombre, edad, nivel_urgencia):
        paciente = {"nombre": nombre, "edad": edad, "nivel_urgencia": nivel_urgencia}
        if nivel_urgencia == 1:
            self.critical_queue.enqueue(paciente)
        elif nivel_urgencia == 2:
            self.severe_queue.enqueue(paciente)
        elif nivel_urgencia == 3:
            self.mild_queue.enqueue(paciente)
            self.quick_review_queue.enqueue(paciente)  # También lo colocamos en la cola rápida
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
        
        # Agregar al historial
        self.historial.agregar_final(paciente)
        # Crear pila para medicamentos
        self.medicamentos_pacientes[paciente["nombre"]] = Pila()
        print(f"Paciente {paciente['nombre']} atendido.")

    def visualizar_historial(self):
        print(f"Historial de Atención: {self.historial}")

    def administrar_medicamento(self, nombre_paciente, medicamento):
        if nombre_paciente in self.medicamentos_pacientes:
            self.medicamentos_pacientes[nombre_paciente].push(medicamento)
            print(f"Medicamento {medicamento} administrado a {nombre_paciente}.")
        else:
            print(f"El paciente {nombre_paciente} no existe en el historial.")

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
            print("4. Administrar Medicamento")
            print("5. Activar Revisión Rápida")
            print("6. Salir")
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
                nombre = input("Nombre del Paciente: ")
                medicamento = input("Nombre del Medicamento: ")
                self.administrar_medicamento(nombre, medicamento)
            elif opcion == "5":
                self.activar_revision_rapida()
            elif opcion == "6":
                print("Saliendo del programa.")
                break
            else:
                print("Opción inválida, intente nuevamente.")

# Ejecutar el programa
hospital = Hospital()
hospital.menu()
