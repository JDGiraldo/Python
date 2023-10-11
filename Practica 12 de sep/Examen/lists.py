# Importar la clase "node" desde la biblioteca "nodes"
from node import node

#Crear una Pila
class Stack:
    #Constructor de la pila
    def __init__(self):
        self.first = None #Primer elemento de la pila
        self.top = None #Cima o tope de la pila (ultimo elemento)
        self.size = 0 #Tamaño de la pila o cantidad de elementos
    
    #Operacion para verificar si la pila esta vacia
    def Empty(self):
        return self.top == None
    
    #Operacion para apilar
    def Push(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido. no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la pila está vacía
            if self.Empty():
                # Operación para insertar un elemento en una pila vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.top = newNode
            else:
                # Operación para insertar un elemento al final de la pila (PUSH)
                # Paso 3 en el algoritmo
                self.top._next = newNode
                # Paso 4 en el algoritmo
                self.top = newNode
            # Actualizar el tamaño de la lista
            self.size += 1

    
    #Operacion para mostrar la pila
    def Show(self):
        aux = self.first
        while aux:
            print(aux, end=", ")
            aux= aux._next
        print("")
    
    #Operacion para Buscar Elementos en una pila
    def Search(self, data):
        aux = self.first
        while aux:
            if aux.data == str(data):
                return True
            aux = aux._next
        return False