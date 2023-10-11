#importar la clase de la biblioteca de lists
from lists import DoubleLinkedlist

#Crear la instalcia de la lista doblemente enlzada
lista = DoubleLinkedlist()

#Ingresar un elemento en la lista doblemente enlzada
lista.InsertFirst(88)

#Mostrar la lista
print("Lista con un solo elemento")
lista.Show()

#Adicionar un elemento al inicio de la lista
lista.InsertFirst(10)

#Mostrar la lista
print("Lista con un elemento insertado al inicio ")
lista.Show()

#Adicionar un elemento al final de la lista
lista.InsertLast(29)

#Mostrar la lista
print("Lista con un elemento insertado al Final ")
lista.Show()

#Adicionar elemento en cualquier parte
lista.Insert(15,88)

#Mostrar la lista
print("Lista con un elemento insertado al en cualquier parte de la lista ")
lista.Show()

print("Ultimo elemento", lista.last)