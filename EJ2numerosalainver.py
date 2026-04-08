import random

class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("Fin")

    def mostrar_inversa(self, nodo):
        if nodo is None:
            return

        self.mostrar_inversa(nodo.siguiente)

        print(nodo.dato, end=" -> ")



lista_ejercicio2 = ListaEnlazada()

for _ in range(100):
    num = random.randint(1, 200) 
    lista_ejercicio2.insertar_al_final(num)

print("Lista normal chaval")
lista_ejercicio2.mostrar()

print("Lista Invertida")
lista_ejercicio2.mostrar_inversa(lista_ejercicio2.cabeza)
print("Inicio")