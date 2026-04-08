from EJ2numerosalainver import ListaEnlazada

lista_m = ListaEnlazada()
lista_n = ListaEnlazada()
lista_p = ListaEnlazada()

print("Configuración de Listas")
m_cantidad = int(input("¿Cuántos números para la lista M?: "))
n_cantidad = int(input("¿Cuántos números para la lista N?: "))


print("Ingresa los valores para la lista M:")
for i in range(m_cantidad):
    valor = float(input(f"Valor M[{i+1}]: "))
    lista_m.insertar_al_final(valor)


print("Ingresa los valores para la lista N:")
for i in range(n_cantidad):
    valor = float(input(f"Valor N[{i+1}]: "))
    lista_n.insertar_al_final(valor)


actual_m = lista_m.cabeza
while actual_m:

    actual_n = lista_n.cabeza
    while actual_n:
        producto = actual_m.dato * actual_n.dato
        lista_p.insertar_al_final(producto)
        actual_n = actual_n.siguiente
    actual_m = actual_m.siguiente


print("Resultados")
print("Lista M:", end=" ")
lista_m.mostrar()
print("Lista N:", end=" ")
lista_n.mostrar()
print("Lista P (Todos los productos posibles):", end=" ")
lista_p.mostrar()