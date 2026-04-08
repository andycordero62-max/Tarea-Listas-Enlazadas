class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

class ListaInteractiva:
    def __init__(self):
        self.cabeza = None

    def insertar_final(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def insertar_posicion(self, valor, pos):
        nuevo = Nodo(valor)
        if pos == 0:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
            return
        
        actual = self.cabeza
        indice = 0
        while actual and indice < pos - 1:
            actual = actual.siguiente
            indice += 1
        
        if actual:
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            print("Posición fuera de rango.")

    def eliminar_posicion(self, pos):
        if not self.cabeza: return

        if pos == 0:
            self.cabeza = self.cabeza.siguiente
            return

        actual = self.cabeza
        indice = 0
        while actual.siguiente and indice < pos - 1:
            actual = actual.siguiente
            indice += 1
        
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente
        else:
            print("Posición no encontrada.")

    def reportar(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía.")
            return
        while actual:
            print(f"[{actual.dato}]", end=" -> ")
            actual = actual.siguiente
        print("None")

    def contar(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

mi_lista = ListaInteractiva()

while True:
    print(".....MENÚ DE OPERACIONES.....")
    print("a. Crear lista (Reiniciar)")
    print("b. Insertar al final")
    print("c. Insertar en una posición")
    print("d. Eliminar de una posición")
    print("e. Reportar")
    print("f. Obtener número de elementos")
    print("g. Salir")
    
    opcion = input("\nSeleccione una opción: ").lower()

    if opcion == 'a':
        mi_lista = ListaInteractiva()
        print("Lista reiniciada (vacía).")
    elif opcion == 'b':
        val = float(input("Ingrese el número real: "))
        mi_lista.insertar_final(val)
    elif opcion == 'c':
        val = float(input("Ingrese el valor: "))
        p = int(input("Ingrese la posición (empieza en 0): "))
        mi_lista.insertar_posicion(val, p)
    elif opcion == 'd':
        p = int(input("Ingrese la posición a eliminar: "))
        mi_lista.eliminar_posicion(p)
    elif opcion == 'e':
        mi_lista.reportar()
    elif opcion == 'f':
        print(f"Total de elementos: {mi_lista.contar()}")
    elif opcion == 'g':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")