import random as rn

class Pedido:

    def __init__(self, tipo, prioridad, destino, codigo, cliente):

        self.tipo = int(tipo)         # 1 = Nacional, 2 = Internacional
        self.prioridad = int(prioridad)  # 1 = Urgente, 2 = Normal
        self.destino = str(destino)
        self.codigo = str(codigo)
        self.cliente = str(cliente)
        self.siguiente = None

class ListaDePedidos:

    def __init__(self):

        self.cabeza = None
        self.cola = None

    def codigo(self):

        cod = f"{rn.randint(0, 9)}{rn.randint(0, 9)}{rn.randint(0, 9)}{rn.randint(0, 9)}"
        return cod

    def agregar(self, tipo, prioridad, destino, cliente):

        codigo = self.codigo()
        nuevoPedido = Pedido(tipo, prioridad, destino, codigo, cliente)

        if self.cabeza is None:

            self.cabeza = self.cola = nuevoPedido

        else:

            actual = self.cabeza
            anterior = None

            while actual is not None:

                if actual.prioridad < nuevoPedido.prioridad:

                    anterior = actual
                    actual = actual.siguiente

                elif actual.prioridad == nuevoPedido.prioridad:

                    if actual.tipo <= nuevoPedido.tipo:

                        anterior = actual
                        actual = actual.siguiente

                    else:

                        break
                else:

                    break

            if anterior is None:

                nuevoPedido.siguiente = self.cabeza
                self.cabeza = nuevoPedido

            else:

                nuevoPedido.siguiente = anterior.siguiente
                anterior.siguiente = nuevoPedido

                if nuevoPedido.siguiente is None:
                    
                    self.cola = nuevoPedido

        print(f"Pedido generado con exito, su codigo es {nuevoPedido.codigo}")

    def imprimirLista(self):

        i = 0
        actual = self.cabeza
        while actual is not None:

            i += 1
            
            if actual.tipo == 1:

                tipo = "Nacional"

            else:
                
                tipo = "Internacional"

            if actual.prioridad == 1:
                
                prioridad = "Urgente"
                
            else:
                
                prioridad = "Normal"

            print(f"{i}. \t {prioridad} \t {tipo} \t {actual.destino} \t {actual.codigo} \t {actual.cliente}")

            actual = actual.siguiente
    
    def eliminar(self, codigo):

        actual = self.cabeza
        anterior = None

        while actual is not None:

            if actual.codigo == codigo:

                if anterior is None:

                    self.cabeza = actual.siguiente

                    if self.cabeza is None:
                        
                        self.cola = None

                else:

                    anterior.siguiente = actual.siguiente

                    if actual == self.cola:

                        self.cola = anterior

                print(f"Pedido con codigo {codigo} eliminado correctamente.")
                return

            anterior = actual
            actual = actual.siguiente

        print(f"Pedido con codigo {codigo} no encontrado.")
    
    def reporte_totales(self):

        nat_urg = nat_norm = int_urg = int_norm = 0

        actual = self.cabeza
        while actual is not None:

            if actual.tipo == 1 and actual.prioridad == 1:
                nat_urg += 1

            elif actual.tipo == 1 and actual.prioridad == 2:
                nat_norm += 1

            elif actual.tipo == 2 and actual.prioridad == 1:
                int_urg += 1

            elif actual.tipo == 2 and actual.prioridad == 2:
                int_norm += 1

            actual = actual.siguiente

        print("\n--- Reporte de Totales ---")
        print(f"Nacionales Urgentes: {nat_urg}")
        print(f"Nacionales Normales: {nat_norm}")
        print(f"Internacionales Urgentes: {int_urg}")
        print(f"Internacionales Normales: {int_norm}")

    def procesar_pedidos(self):

        historial = PilaHistorial()

        while self.cabeza is not None:

            procesado = self.cabeza
            self.cabeza = self.cabeza.siguiente

            if self.cabeza is None:

                self.cola = None
            print(f"Procesando pedido: {procesado.codigo} ({procesado.destino} - {procesado.cliente})")
            historial.push(procesado)
        historial.mostrar()

class NodoHistorial:

    def __init__(self, pedido):

        self.pedido = pedido
        self.siguiente = None

class PilaHistorial:

    def __init__(self):

        self.tope = None

    def push(self, pedido):

        nuevo = NodoHistorial(pedido)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    def mostrar(self):

        actual = self.tope
        i = 1

        print("\n--- Historial de pedidos procesados (último al primero) ---")

        while actual:

            p = actual.pedido
            tipo_txt = "Nacional" if p.tipo == 1 else "Internacional"
            prioridad_txt = "Urgente" if p.prioridad == 1 else "Normal"
            print(f"{i}. {prioridad_txt} - {tipo_txt} - {p.destino} - {p.codigo} - {p.cliente}")
            actual = actual.siguiente
            i += 1

compañia = ListaDePedidos()
compañia.agregar(1, 1, "Cartagena", "Luis")
compañia.agregar(2, 2, "Bogotá", "Ana")
compañia.agregar(1, 2, "Barranquilla", "Pedro")
compañia.agregar(2, 1, "Madrid", "Carlos")
compañia.agregar(1, 1, "Santa Marta", "Juan")

compañia.imprimirLista()
compañia.reporte_totales()

print("\n¿Deseas procesar todos los pedidos? (s/n)")

if input().lower() == "s":
    compañia.procesar_pedidos()
