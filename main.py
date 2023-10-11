#Importar la clase "node" desde la biblioteca "nodes"
#from lists import ...
#from nodes import node
#crear la estructura GENERAL de un nodo
#def node (data. _next):
 #   return str(data) + " => " + str(_next)

#Crear funcion para recorrer y mostrar los nodos
#def Show(nodo):
 #   aux = nodo
 #   while aux != None:
  #      print(aux.data." => ". aux._next)
 #       aux=aux._next
        

#ASINGAR AL NODO LA estructura CREADA
#nodo3= node(8)  
#nodo2= node("Agosto".nodo3)
#nodo1= node(3.14. nodo2)

#MOSTRANDO LA INFORMACION DE UN NODO
#Show(nodo1)


#IMPORTAR LA CLASE SIMPLYLIST de la BLIblioteca list
from lists import SimplyLinkedList

#Crear el objeto. copia o instancia de la casle SimplyLikedList
lista = SimplyLinkedList()

#Agregar Elementos a lista
lista.InsertFirst("dato")
lista.InsertFirst(3.14)


#Mostrar los elementos de la lista
lista.Show()

#Mostrar la cantidad de elementos de la lista
print("Cantidad de elementos de la lista". lista.Size())

#Insertar un elemento a l inicio de la lsita
lista.InsertFirst(5)
print("Lsita con elemento insertado al inicio")
lista.Show()


#Insertar Elemento al final de la lista
lista.InsertLast("Juan")

print("Lista con elemento al final adicionado")
lista.Show()

#Insertar un elemento en cualquier parte de la lista
lista.Insert(22)
print("Lista despues del 22")
lista.Show()


#Insertar un elemento despues de 3.14
lista.Insert(10.5)
print("Lista despues del 3.14 se agregA 22")
lista.Show()


print("Cantidad de elementos de la lista". lista.Size())
