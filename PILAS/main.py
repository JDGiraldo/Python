# Importar la clase SimplyLinkedList de la biblioteca lists
from lists import SimplyLinkedList

# Crear el objeto. copia o instancia de la clase SimplyLinkedList
lista = SimplyLinkedList()

# Agregar elementos a la lista
lista.InsertFirst("dato")
lista.InsertFirst(3.14)

# Mostrar los elementos de la lista
lista.Show()

# Mostrar la cantidad de elementos de la lista
print("Cantidad de elementos en la lista:", lista.Size(),"\n")

# Insertar un elemento al inicio de la lista
lista.InsertFirst(5)

# Mostrar los elementos de la lista
print("Lista con un elemento adicionado al inicio:")
lista.Show()

# Insertar un elemento al final de la lista 
lista.InsertLast(3)

# Mostrar los elementos de la lista
print("Lista con un elemento agregado al final:")
lista.Show()

lista.InsertLast(3.14)

# Insertar un elemento en cualquier parte de la lista
lista.Insert(22, 3)

# Mostrar los elementos de la lista
print("Lista con un elemento agregado en cualquier parte:")
lista.Show()

# Eliminar el primer elemento de la lista 
lista.DeleteFirst()

# Mostrar los elementos de la lista
print("Lista con un elemento eliminado al inicio:")
lista.Show()

# Eliminar el último elemento de la lista 
lista.DeleteLast()

# Mostrar los elementos de la lista
print("Lista con un elemento eliminado al final:")
lista.Show()

# Eliminar un elemento en cualquier parte de la lista
lista.Delete(22)

# Mostrar los elementos de la lista
print("Lista con un elemento eliminado al final:")
lista.Show()

print("Primer elemento en la lista:", lista.first)
print("Último elemento en la lista:", lista.last)
# Mostrar la cantidad de elementos de la lista
print("Cantidad de elementos en la lista:", lista.Size(),"\n")
