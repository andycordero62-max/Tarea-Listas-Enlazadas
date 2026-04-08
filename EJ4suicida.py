class NodoCirculito:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

class ListaCirculito:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre):
        nuevo = NodoCirculito(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
            nuevo.siguiente = self.cabeza 
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.siguiente = self.cabeza 

    def algoritmo_suicidas(self, n):
        for i in range(1, n + 1):
            self.agregar(f"Persona {i}")
        
        actual = self.cabeza
        print(f"Empieza el círculo con {n} personas.")

        while actual.siguiente != actual:

            eliminado = actual.siguiente
            print(f"{actual.dato} elimina a {eliminado.dato}")
            

            actual.siguiente = eliminado.siguiente
            

            actual = actual.siguiente
        
        print(f"--- EL SOBREVIVIENTE ES: {actual.dato} ---")

n = int(input("¿Cuántas personas hay en el círculo?: "))
juego = ListaCirculito()
juego.algoritmo_suicidas(n)