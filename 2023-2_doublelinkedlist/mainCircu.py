# Importar la clase Queue de la biblioteca lists
from lists import CircularLinkedList
from os import system

lista = CircularLinkedList()

lista.InsertFirst("Mie")
lista.InsertFirst("Mar")
lista.InsertFirst("Lun")

lista.Show()

lista.InsertLast("Jue")
lista.InsertLast("Vie")
lista.InsertLast("Sab")

print("Lista con elementos nuevos al final")
lista.Show()

lista.Insert("Dom","Sab")

print("Lista con elementos nuevos en cuaquier parte")
lista.Show()

print("Puntero siguiente del primer elemento", lista.first._next)
print("Puntero siguiente del ultimo elemento", lista.last._next)
print("ultimo elemento", lista.last)

lista.Delete("Jue")

print("Lista con un elemento en cualquier parte: ")
lista.Show()