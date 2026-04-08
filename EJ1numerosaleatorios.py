import random

class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_ordenado(self, valor):
        nuevo_nodo = Nodo(valor)
        
        if self.cabeza is None or self.cabeza.dato >= valor:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None and actual.siguiente.dato < valor:
                actual = actual.siguiente
            
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos))

lista_principal = ListaEnlazada()
lista_menores_100 = ListaEnlazada()

for _ in range(10): 
    num = round(random.uniform(1, 1500), 2) 
    lista_principal.insertar_ordenado(num)

print("Lista Principal (Ordenada):")
lista_principal.mostrar()

actual = lista_principal.cabeza
while actual:
    if actual.dato < 100:
        lista_menores_100.insertar_ordenado(actual.dato)
    actual = actual.siguiente

print("\nSegunda Lista (Valores menores que 100):")
lista_menores_100.mostrar()