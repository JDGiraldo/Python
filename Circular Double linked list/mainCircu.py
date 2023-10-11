# Importar la clase Queue de la biblioteca lists
from lists import CircularDoublyLinkedList
from os import system

lista = CircularDoublyLinkedList()

lista.InsertFirst("Mie")
lista.InsertFirst("Mar")
lista.InsertFirst("Lun")

lista.ShowInitToEnd()


lista.InsertLast("Jue")
lista.InsertLast("Vie")
lista.InsertLast("Sab")

print("Lista con elementos nuevos al final")
lista.ShowInitToEnd()


lista.Insert("Dom","Lun")

print("Lista con elementos nuevos en cuaquier parte")
lista.ShowInitToEnd()
lista.ShowEndToInit()

print("Puntero siguiente del primer elemento", lista.first._next)
print("Puntero siguiente del ultimo elemento", lista.last._next)
print("ultimo elemento", lista.last)

lista.DeleteFirst()
lista.ShowInitToEnd()
lista.ShowEndToInit()

'''
lista.Delete("Jue")

print("Lista con un elemento en cualquier parte: ")
lista.Show()'''