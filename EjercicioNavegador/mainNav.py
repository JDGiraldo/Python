# Importar la clase Queue de la biblioteca lists
from lists import DoubleLinkedList

# Crear la instancia de la lista doblemente enlazada
lista = DoubleLinkedList()

while True:
    lista.ShowInitToEnd()
    op = input().split()
    if op[0] == "n":
        lista.InsertLast(op[1])
    elif op[0] == "a":
        for elem in op:
            if elem == "a":
                lista.Navg("a")
            elif elem == "p":
                lista.Navg("p")
    elif op == "0":
        break
lista.Getpag()