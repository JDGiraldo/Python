# Importar la clase Queue de la biblioteca lists
from lists import DoubleLinkedList
from os import system

# Crear la instancia de la lista doblemente enlazada
lista = DoubleLinkedList()

# Ingresar un elemento en la lista doblemente enlazada
lista.InsertFirst(88)
lista.InsertFirst(77)
lista.InsertFirst(55)
lista.InsertFirst(20)
lista.InsertFirst(18 )

# Mostrar la lista
print("Lista con un solo elemento:")
lista.ShowInitToEnd()

# Adicionar un elemento al inicio de la lista
lista.InsertFirst(10)

# Mostrar la lista
print("Lista con un elemento insertado al inicio:")
lista.ShowInitToEnd()

# Adicionar un elemento al final de la lista
lista.InsertLast(29)

# Mostrar la lista
print("Lista con un elemento insertado al final:")
lista.ShowInitToEnd()

# Adicionar un elemento en cualquier parte de la lista
lista.Insert(15, 10)

# Mostrar la lista
print("Lista con un elemento insertado en cualquier parte:")
lista.ShowInitToEnd()

#Eliminar un element al inicio de la lista
lista.DeleteFirst()

print("Lista con un elemento eliminado al inicio:")
lista.ShowInitToEnd()

#Eilimar un eleemento al final de la lista
lista.DeleteLast()

print("Lista con un elemento eliminado al final:")
lista.ShowInitToEnd()

#eleimianr un elemento en cualquier parte de la lita
lista.Delete(55)

print("Lista recorrida al inicio a fin")
lista.ShowInitToEnd()

print("Lista recorrida al fin a inicio")
lista.ShowEndToInit()

print("Último elemento en la lista:", lista.last)

print("Cantidad de elementos en la lista:", lista.size)
