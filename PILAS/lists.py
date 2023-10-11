# Importar la clase "node" desde la biblioteca "nodes"
from nodes import node

# Crear la clase Lista Simplemente Enlazada
class SimplyLinkedList:
    
    # Constructor de la clase
    def __init__(self):
        self.first = None # Nodo inicio o nodo primero
        self.last = None # Nodo fin o nodo último
        self.size = 0 # Tamaño de la lista
    
    # Método para verificar si la lista está vacía o no
    def Empty(self):
        return self.first == None
    
    # Método para insertar un elemento al inicio de la lista
    def InsertFirst(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido. no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
            else:
                # Operación para insertar un elemento al inicio de la lista
                # Paso 3 en el algoritmo
                newNode._next = self.first
                # Paso 4 en el algoritmo
                self.first = newNode
            # El tamaño se actualiza
            self.size += 1
    
    # Método para insertar elementos al final de la lista
    def InsertLast(self, data = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido. no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
            else:
                # Operación para insertar un elemento al final de la lista
                # Paso 3 en el algoritmo
                self.last._next = newNode
                # Paso 4 en el algoritmo
                self.last = newNode
            # Actualizar el tamaño de la lista
            self.size += 1
    
    # Operación para insertar un elemento en cualquier parte de la lista
    def Insert(self, data = None, position = None):
        # Verificar si se ingresó un dato válido
        if data == None:
            print("¡Error! No se ingresó un dato válido. no es posible adicionar el elemento en la lista.") 
        else:
            # Asignar memoria y rellenar el campo de datos
            newNode = node(data)
            # Verificar si la lista está vacía
            if self.Empty():
                # Operación para insertar un elemento en una lista vacía
                # Los punteros inicio y fin apuntarán hacia el nuevo elemento
                self.first = self.last = newNode
                # Actualizar el tamaño de la lista
                self.size += 1
            # Verificar si no se ingresó un valor en la posición
            elif position == None:
                # Si no hay una posición. por defecto se adiciona el elemento al
                # final de la lista
                self.InsertLast(data)
            # Validar si no se encuentra la posición ingresada en la operación
            elif not self.Search(position):
                print("¡Error! No se encontró la posición ingresada en la operación. no es posible ingresar el dato.")
            # Ejecutar la operación para ingresar un elemento en cualquier
            # parte de la lista
            else:
                # Paso 3: Encontrar la posición en la lista para insertar el nodo.
                aux = self.first
                while aux:
                    if aux.data == str(position):
                        # Paso 4 del algoritmo
                        newNode._next = aux._next
                        # Paso 5 del algoritmo
                        aux._next = newNode
                        # Validar si el nuevo nodo es el nuevo último elemento
                        # elemento de la lista
                        if newNode._next == None:
                            self.last = newNode
                        # Actualizar el tamaño de la lista
                        self.size += 1
                        break
                    aux = aux._next

    # Operación para eliminar un elemento al inicio de la lista
    def DeleteFirst(self):
        # Validar si la lista está vacía
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento en una lista vacía.")
        # Validar si queda un solo elemento en la lista
        elif self.first == self.last:
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -= 1
        # Operación eliminar un elemento al inicio de la lista
        else:
            self.first = self.first._next
            # Actualizar el tamaño de la lista
            self.size -= 1
    
    # Operación para eliminar el último elemento de la lista
    def DeleteLast(self):
        # Validar si la lista está vacía
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento en una lista vacía.")
        # Validar si queda un solo elemento en la lista
        elif self.first == self.last:
            self.first = self.last = None
            # Actualizar el tamaño de la lista
            self.size -= 1
        # Operación eliminar un elemento al final de la lista
        else:
            # Paso 1 ya está listo. el puntero último (self.last) almacena
            # al elemento que se desea eliminar
            # Paso 2 en el algoritmo
            aux = self.first
            while aux._next != self.last:
                aux = aux._next
            # Paso 3 en el algoritmo
            aux._next = self.last._next
            # Paso 4 en el algoritmo
            self.last = aux
            # Actualizar el tamaño de la lista
            self.size -= 1

    #Borrar cualquier elemento de la lista
    def Delete(self, data=None):
        #Valirdar si la lista esta vacia
        if self.Empty():
            print("Error No es posible eliminar un elemento de una lista vacia")
        #VAlidar si queda un solo elemento en la lista
        elif self.first ==self.last:
            self.first = self.last = None
            #Actualizar el tamaño de la lista
            self.size -=1
        #VAlidar si no se ingreso un dato a elimar
        elif not data:
            #Por defecto voy a eliminar el ultimo dato de la lista
            self.DeleteLast()
        #Validar si el elemento que voy a eliminar es el primero de lista
        elif str(data) == self.first.data:
            #Eliminar el primer elemento de la lista
            self.DeleteFirst()
        #Verificar si el elemento existe 
        elif not self.Search(data):
            print("Error el elemento ingresado no existe en la lista. no es posible eliminarlo")
        #Operacion eliminar un elemento en cualquier parte de lalista
        else:
            #Paso 1 en el algoritmo
            aux= self.first
            while aux._next.data != str(data):
                aux = aux._next
            #Paso 2 en algoritmo
            aux._next=aux._next._next
            #validar si el elemento acutal es el penultimo en la lista 
            if aux._next == None:
                self.last = aux
            #Actualizar el tamaño de la lista
            self.size -= 1

    # Operación para mostrar la lista
    def Show(self):
        if self.Empty():
            print("La lista está vacía.")
        else:
            aux = self.first
            while aux:
                print(aux.data," ",end="")
                aux = aux._next
            print("\n")
    
    # Operación para buscar un dato en la lista
    def Search(self, data):
        aux = self.first
        while aux:
            if str(data) == aux.data:
                return True
            aux = aux._next
        return False

    # Operacion para mostrar el tamaño de la lista
    def Size(self):
        return self.size
        
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

    # Operación para desapilar un elemento de la pula
    def Pop(self):
        # Validar si la pila está vacía
        if self.Empty():
            print("¡Error! No es posible eliminar un elemento en una lista vacía.")
        # Validar si queda un solo elemento en la pila
        elif self.first == self.top:
            data= self.top.data
            self.first = self.top = None
            # Actualizar el tamaño de la pila
            self.size -= 1
        # Operación eliminar un elemento al final de la pila (pop)
        else:
            data= self.top.data
            # Paso 1 ya está listo. el puntero último (self.top) almacena
            # al elemento que se desea eliminar
            # Paso 2 en el algoritmo
            aux = self.first
            while aux._next != self.top:
                aux = aux._next
            # Paso 3 en el algoritmo
            aux._next = self.top._next
            # Paso 4 en el algoritmo
            self.top = aux
            # Actualizar el tamaño de la lista
            self.size -= 1
        return data
    
    #Operacion para tener la cima de la pila
    def Top(self):
        return self.top

     # Operacion para mostrar el tamaño de la pila
    def Size(self):
        return self.size

    #Operacion para mostrar la pila
    def Show(self):
        aux = self.first
        while aux:
            print(aux)
            aux= aux._next
    
    