#Implementar un reproductor musical haciendo uso de una doble

# Importar la clase Queue de la biblioteca lists
from lists import DoubleLinkedList
from os import system

# Crear la instancia de la lista doblemente enlazada
lista = DoubleLinkedList()

# Ingresar un elemento en la lista doblemente enlazada
lista.Insert("Tabaco y Ron")
lista.Insert("La Flaca")
lista.Insert("Juanito Alimaña")
lista.Insert("La Rebelion")
lista.Insert("One")
lista.Insert("El Cantante")

while True:
   
    lista.ShowInitToEnd()
    if  lista.GetSong():
        print("-" *50)
        print("Cancion en reproducción: ", lista.GetSong())
        print("-" *50)
    #Escribir un codigo
    print("")
    print("Menu de opciones:")
    print("1. Reproducir cancion inicial")
    print("2. Cancion Siguiente")
    print("3. Cancion Anterior")
    print("4. Adicionar cancion Nueva al final")
    print("5. Pausar/Reanudar")
    print("9. Salir")
    op = input("Ingrese la opción deseada: ") 
    if op == "1":
        lista.Play()
    elif op == "2":
        lista.Play("n")
    elif op == "3":
        lista.Play("b")
    elif op == "4":
        ingre = input("Insertar Cancion")
        lista.Insert(ingre)
    elif op == "0":
        break

print("\nFin")
